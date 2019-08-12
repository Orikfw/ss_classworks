from random import random
"""Роздрукувати всі парні числа менші 100"""
#використовуючи цикл for
list_of_even1 = []
for i in range(100):
    if i % 2 == 0:
        list_of_even1.append(i)
print('Парні числа: ', list_of_even1)

#в одну стрічку
print('Парні числа: ', list(range(0, 100, 2)))

#використовуючи цикл while
list_of_even2 = []
count = 0 
while count < 100:
    if count % 2 == 0:
        list_of_even2.append(count)
    count += 1
print('Парні числа: ', list_of_even2)


"""Роздрукувати всі непарні числа менші 100"""
#використовуючи оператор continue
list_of_odd1 = []
for i in range(100):
    if i % 2 == 0:
        continue
    list_of_odd1.append(i)
print('Непарні числа: ', list_of_odd1)

#без оператора
list_of_odd2 = []
for i in range(100):
    if i % 2 != 0:
        list_of_odd2.append(i)
print('Непарні числа: ', list_of_odd2)


"""Перевірити чи список містить непарні числа(оператор break)"""  
for i in list(range(10)):
    if i % 2 != 0:
        print('Так, список містить непарні числа')
        break
else:
    print('Ні, непарних числе немає')


"""Створити цілочисельний список, змінити тип даних на float"""
#використовуючи новий список, безіндексний цикл
my_list_int = list(range(20))
new_list = []
for i in my_list_int:
    new_list.append(float(i))
print(new_list)

#переписуючи список за індексами
for i in range(len(my_list_int)):
    my_list_int[i] = float(my_list_int[i])
print(my_list_int)


"""Вивести числа Фібоначі включно до введеного числа"""
end = int(input('Введіть кінцеве число послідовності:\n'))
fib = [0 , 1]
for index in range(2, end + 1):
    fib.append(fib[index - 1] + fib[index - 2])
print(fib)


"""Створити список, вивести елементи по черзі,
змінити програму, щоб при виводі додавалась #
"""
my_list_str = ['first', 'second', 'third', 'fourth']
#вивід елементів по черзі
for word in my_list_str:
    print(word)

#вивід елементів з символом
for word in my_list_str:
    print(word, end='#')


"""Перевірити чи число просте"""
number_to_check = int(input('Введіть число яке бажаєте перевірити:\n'))
if ((157 ** number_to_check) - 157) % number_to_check == 0:
    print(f'Так, число {number_to_check} - просте!')
else:
    print(f'Ні, число {number_to_check} - складне..')


"""Знайти максимальну цифру дійсного числа"""
number = str(random())
print(f'Згенероване число: {number}')
max_num = 0
for i in range(len(number)):
    if number[i] == '.':
        continue
    if int(number[i]) > max_num:
        max_num = int(number[i])
print(f'Максимальна цифра: {max_num}')


"""Визначити чи слово паліндром"""
word_pol = list(str(input('Введіть слово яке бажаєте перевірити:\n')).lower())
rev_word = word_pol.copy()
rev_word.reverse()
if word_pol == rev_word:
    print('Так, введене слово - паліндром!')
else:
    print('Ні, введене слово не паліндром..')
