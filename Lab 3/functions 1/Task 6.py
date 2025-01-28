def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

user_sentence = input("Введите предложение: ")
reversed_sentence = reverse_sentence(user_sentence)
print("Предложение с перевернутым порядком слов:")
print(reversed_sentence)
