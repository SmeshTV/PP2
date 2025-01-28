def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

user_input = input("Введите слово или фразу: ")
if is_palindrome(user_input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")
