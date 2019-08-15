import math
"""Тест функції all()"""
mylist = [True, True, True]
x = all(mylist)
print(x)

mylist = [0, 1, 1]
x = all(mylist)
print(x)


"""Створити список цілих чисел, та знайти серед них мінімальне та максимальне"""
try:
    my_lits = [int(input(f'Введіть {i+1} ціле числo: ')) for i in range(int((input('Введіть розмір списку: '))))]
    print(f'Максимум: {max(my_lits)}\nМінімум: {min(my_lits)}')
except ValueError:
    print('Будь ласка, вводьте цілі числа!') 


"""В інтервалі від 1 до 10 визначити числа 
•  парні, які діляться на 2,
•  непарні, які діляться на 3, 
•  числа, які не діляться на 2 та 3.
"""
print(f'Парні які діляться на 2: {list(range(0, 11, 2))}')
print(f'Непарні які діляться на 3: {[num for num in range(1,11) if num % 2 == 1 and num % 3 == 0]}')
print(f'Числа які не діляться на 2 і 3: {[num for num in range(1,11) if num % 2 != 0 and num % 3 != 0]}')


"""Факторіал числа що вводить користувач(без рекурсії)"""
try:
    num = input_num = int(input('Введіть число, факторіал якого бажаєте знайти: '))
    if num < 0:
        print('Введіть додатнє число!')
    elif num == 0:
        print('Факторіал 0 = 1')
    else:
        fact = 1
        while num > 0:
            fact = fact * num
            num -=1
        print(f'Факторіал {input_num} = {fact}')
except ValueError:
    print('Введіть ціле число!')


"""Cкрипт, який перевіряє логін, який вводить користувач"""
login = 'First'
while True:
    test  = input('Введіть логін:\n')
    if login == test:
        print('Hello user')
        break
    else:
        print('login incorrect, try again...')


"""Програма зчитує числа поки не зустріне від'ємне число або нуль"""
while True:
    num = int(input('Введіть число: '))
    if num < 0:
        print("Виявлено від'ємне число!")
        break
    elif num == 0:
        print("Виявлено нуль!")
        break


"""На вхід подається к-сть елементів послідовності. Якщо зустрічається від'ємне чи нуль - програма зупиняється"""
try:
    count = int(input('Введіть к-сть елементів послідовності: '))
    i = 1
    while i <= count:
        num = float(input(f'Введіть {i} число послідовності: '))
        if num < 0:
            print("Виявлено від'ємне число!")
            break
        elif num ==0:
            print("Виявлено нуль!")
            break
        i += 1
    else:
        print("Не було виявлено помилок при введенні!")
except ValueError:
    print('Вводьте цілі числа!')


"""Знайти прості числа від 10 до 30, решта представити у вигляді добутку"""
for number_to_check in range(10, 31):
    i = 2
    limit = int(math.sqrt(number_to_check))
    while i <= limit:
        if number_to_check % i == 0:
            print(f'Число {number_to_check} рівне 2 * {number_to_check / 2}')
            break
        i += 1
    else:
        print(f'Число {number_to_check} - просте!')


"""Відсортувати слова в реченні в порядку їх довжини"""
sentence = '''Наша мама мыла раму
              Кто бы вымыл нашу маму
              Вся она в песке и пенке
              Поцарапаны коленки
              Если я вдруг магом стану
              Сможет рама вымыть маму'''
sorted_sentence = [word for word in sorted(sentence.split(), key=lambda a: len(a))]
print(sorted_sentence)