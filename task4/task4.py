import sys
# Запуск скрипта --python task4.py numbers.txt--

def main():
    # Чтение чисел из файла
    with open(sys.argv[1], 'r') as file:
        nums = []
        for line in file:
            nums.append(int(line.strip()))

    median = sorted(nums)[len(nums) // 2]
    print(sum(abs(num - median) for num in nums))

if __name__ == "__main__":
    main()