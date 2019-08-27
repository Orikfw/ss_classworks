import pyowm
import random
import math

owm = pyowm.OWM('33090165cfd01a96ecf247cc9b3b86d7')
print('*' * 100)
print('Привіт! Вибери місто, погоду у якому бажаєш дізнатись!')
city = str(input())
observation = owm.weather_at_place(city)
w = observation.get_weather()

print(f"""Погода станом на {w.get_reference_time(timeformat='iso')}:
Статус: {w.get_status()}
Температура: {w.get_temperature('celsius')['temp']}градусів Цельсія
Швидкість вітру: {w.get_wind()['speed']}м/с
Вологість: {w.get_humidity()}%""")
print('*' * 100)


"""Вгадай число"""
print('Вгадай число :)')
num = random.randint(1, 101)
while True:
    in_num = int(input())
    if in_num < num:
        print('Загадане число більше!')
        continue
    elif in_num > num:
        print('Загадане число менше!')
        continue
    elif in_num == num:
        print('Вітаємо, Ви виграли!')
        break


"""Написати програму, яка обчислює площу прямокутника, трикутника та кола 
(написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)
"""
def s_priam(a, b):
    return a * b

def s_triangle(a, h):
    return 0.5 * a * h

def s_circkle(r):
    return math.pi * math.pow(r, 2)

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