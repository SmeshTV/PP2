import random

def guess_the_number():
    print("Привет! Как тебя зовут?")
    name = input("Введите имя: ")
    
    print(f"Ну что, {name}, я загадал число от 1 до 20. Попробуй угадать!")
    number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Ваше предположение: "))
        attempts += 1
        
        if guess < number:
            print("Ваше число меньше загаданного.")
        elif guess > number:
            print("Ваше число больше загаданного.")
        else:
            print(f"Отлично, {name}! Вы угадали число {number} за {attempts} попыток!")
            break

guess_the_number()
