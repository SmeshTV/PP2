def histogram(numbers):
    for num in numbers:
        print('*' * num)

numbers = list(map(int, input("Введите числа через пробел: ").split()))
print("Гистограмма:")
histogram(numbers)
