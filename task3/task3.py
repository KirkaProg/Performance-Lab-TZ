import sys, json
# Запуск скрипта по команде --python task3.py values.json tests.json reports.json-- 

def build_values_dict(values_data): # Формирование словаря из values
    values_list = []
    if isinstance(values_data, dict):
        if 'values' in values_data:
            values_list = values_data['values']
    elif isinstance(values_data, list):
        values_list = values_data

    values_dict = {}
    for item in values_list:
        if isinstance(item, dict) and 'id' in item and 'value' in item:
            values_dict[item['id']] = item['value']
    return values_dict

def fill_values(node, values_dict): # Рекурсия, заполняет поле values на основе id
    if isinstance(node, list):
        return [fill_values(item, values_dict) for item in node]
    elif isinstance(node, dict):
        if 'id' in node:
            node_id = node['id']
            if node_id in values_dict:
                node['value'] = values_dict[node_id]
        # Рекурсивно обрабатываем все значения в словаре
        for key in node:
            node[key] = fill_values(node[key], values_dict)
    return node

def main():
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    reports_path = sys.argv[3]

    with open(values_path, 'r', encoding='utf-8') as file:
        values_data = json.load(file)
        values_dict = build_values_dict(values_data)

      # Обработка tests
    with open(tests_path, 'r', encoding='utf-8') as file:
        tests_data = json.load(file)

    # Заполнение полей value
    filled_data = fill_values(tests_data, values_dict)

    # Сохранение отчета
    with open(reports_path, 'w', encoding='utf-8') as file:
        json.dump(filled_data, file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()