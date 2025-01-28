from itertools import permutations

def string_permutations(s):
    perms = [''.join(p) for p in permutations(s)]
    return perms

user_string = input("Введите строку: ")
all_permutations = string_permutations(user_string)
print("Все перестановки строки:")
for perm in all_permutations:
    print(perm)
