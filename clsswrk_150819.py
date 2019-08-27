"""Рекурсивний факторіал"""
def fact(x):
    if x == 1 or x == 0:
        return 1
    else: return x * fact(x - 1)


"""Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел"""
def arf(*args):
    if args == ():
        return ('Порожній список!')
    suma = 0
    for var in args:
        suma += var
    return suma / len(args)
print(arf(10, 50))

def arf_short(*args):
    if args == ():
        return ('Порожній список!')
    return sum(args) / len(args)
print(arf_short(10, 50))


"""Написати функцію, яка повертає абсолютне значення числа"""
def rt_abs(number):
    return abs(number)
print(rt_abs(-5))

def rt_abs_withou_lib(number):
    if number == 0:
        return 0
    elif number > 0:
        return number
    return -number
print(rt_abs_withou_lib(-15))


"""Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings"""
def maximum(fst, scnd):
    """Функція, що повертає максимальне з двох чисел"""
    if fst > scnd:
        print(f'{fst} is max')
    elif fst == scnd:
        print(f'{fst} = {scnd}')
    else:
        print(f'{scnd} is max')
print(maximum.__doc__)
maximum(15, 12)


"""Написати програму, яка обчислює площу прямокутника, трикутника та кола 
(написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)
"""
def s_priam(a, b):
    return a * b

def s_triangle(a, h):
    return 0.5 * a * h

def s_circkle(r):
    return 3.14 * (r ** 2)

while True:
    print('Вітаємо вас у програмі для обчислення площі різних фігур')
    print('*' * 100) 
    print('''Виберіть фігуру, площу якої бажаєте обчислити:
    1 - прямокутник
    2 - трикутник
    3 - коло
    ****************
    4 - вихід з програми''')
    print('*' * 100)
    try: 
        choice = int(input('Ваш вибір: '))
        if choice == 1:
            a = float(input('Введіть довжину сторони а: '))
            if a < 0:
                print('Ой, ну Ви що! Довжина не може бути від\'ємною!')
                print('/' * 100)
                continue
            b = float(input('Введіть довжину сторони b: '))
            if b < 0:
                print('Ой, ну Ви що! Довжина не може бути від\'ємною!')
                print('/' * 100)
                continue
            print(f'Площа прямокутника зі сторонами {a} та {b} дорівнює {s_priam(a, b)}')
            print('/' * 100)
            break
        elif choice == 2:
            a = float(input('Введіть довжину сторони а: '))
            if a < 0:
                print('Ой, ну Ви що! Довжина не може бути від\'ємною!')
                print('/' * 100)
                continue
            h = float(input('Введіть висоту h: '))
            if h < 0:
                print('Ой, ну Ви що! Довжина не може бути від\'ємною!')
                print('/' * 100)
                continue
            print(f'Площа трикутника зі стороною {a} та висотою {h} дорівнює {s_triangle(a, h)}')
            print('/' * 100)
            break
        elif choice == 3:
            r = float(input('Введіть радіус кола r: '))
            if r < 0:
                print('Ой, ну Ви що! Радіус не може бути від\'ємнним!')
                print('/' * 100)
                continue
            print(f'Площа кола з радіусом {r} дорівнює {s_circkle(r)}')
            print('/' * 100)
            break
        elif choice == 4:
            print('Дякуємо за користування. Гарного дня :)')
            break
    except ValueError:
        print('Ой, щось пішло не так...')
        break


"""Написати функцію, яка обчислює суму цифр введеного числа."""
def suma_cifr(num):
    return sum([int(cifra) for cifra in str(num)])
print(suma_cifr(51))


"""Калькулятор"""
def suma(fst, scnd):
    print(f'Результат: {fst + scnd}')
    
def difference(fst, scnd):
    print(f'Результат: {fst - scnd}')

def multiplication(fst, scnd):
    print(f'Результат: {fst * scnd}')
    
def division(fst, scnd):
    try:
        print(f'Результат: {fst / scnd}')
    except ZeroDivisionError:
        print('Ділити на нуль не можна!')
        quit()

print('Вітаємо вас у програмі - калькуляторі')
while True: 
    print('*' * 100) 
    print('''Виберіть дію, яку бажаєте виконати:
    1 - додавання
    2 - віднімання
    3 - множення
    4 - ділення
    ****************
    5 - вихід з програми''')
    print('*' * 100)
    try: 
        choice = int(input('Ваш вибір: '))
        if choice == 5:
            print('Дякуємо, що користувались нашим програмним забезпеченням! Сподіваємось Ви залишились задоволені!')
            print('Гарного дня :)')
            break
        fst = float(input('Введіть перше число: '))
        scnd = float(input('Введіть друге число: '))
        if choice == 1:
            suma(fst, scnd)
            print('*' * 100)
        elif choice == 2:
            difference(fst, scnd)
            print('*' * 100)
        elif choice == 3:
            multiplication(fst, scnd)
            print('*' * 100)
        elif choice == 4:
            division(fst, scnd)
            print('*' * 100)
    except ValueError:
        print('Ой, щось пішло не так...')

"""Рекурсивна ф-ція чисел Фібоначі"""
def fibonachi(n):
    if n <= 1:
        return n
    return fibonachi(n - 1) + fibonachi(n - 2)
for i in range(11):
    print(fibonachi(i))