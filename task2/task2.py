import sys
# Запуски скрипта по команде ниже в консоль
# python task2.py circle.txt dot.txt

def main():
    # Получаем пути из аргументов командной строки
    circle_path = sys.argv[1]
    dots_path = sys.argv[2]

    # Чтение данных окружности
    with open(circle_path, 'r') as file:
        cx, cy = map(float, file.readline().split())
        r = float(file.readline())

    # Чтение данных точек
    dots = []

    with open(dots_path, 'r') as file:
        for line in file:
            if line.strip():
                x, y = map(float, line.split())
                dots.append((x, y))


    # Обработка точек
    r_squared = r * r
    for x, y in dots:
        dx = x - cx
        dy = y - cy
        dist_squared = dx * dx + dy * dy

        if abs(dist_squared - r_squared) < 1e-9:  # Точка на окружности
            print(0)
        elif dist_squared < r_squared:  # Точка внутри
            print(1)
        else:  # Точка снаружи
            print(2)

if __name__ == "__main__":
    main()