number = 23
running = True
while running:
    guess = int(input('Введите целое число : '))

    if guess == number:
        print("Поздравляю вы угадали.")
        running = False # это останавливает цикл while
    elif guess < number:
        print('Нет, загаданое число немного больше этого')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл While закончен.')
    # Здесь можете выполнить все что угодно

print('Завершение.')
