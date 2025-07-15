
def circular_path(n, m):
    flow = []
    current_num = 1  # Первый элемент

    while True:
        flow.append(current_num)
        # Смещаемся на m - 1 шагов вперед, затем +1 обратно
        current_num = ((current_num - 1 + m - 1) % n) + 1
        if current_num == 1:  # Если вернулись к первому элементу — останавливаемся
            break

    return ''.join(map(str, flow))


n, m = map(int, input().split()) # Ввод предпологает наличие пробела между аргементами
print(circular_path(n, m))