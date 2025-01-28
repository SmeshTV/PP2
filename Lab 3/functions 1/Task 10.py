def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

numbers = list(map(int, input("Введите числа через пробел: ").split()))
unique_numbers = unique_elements(numbers)
print("Список с уникальными элементами:", unique_numbers)
