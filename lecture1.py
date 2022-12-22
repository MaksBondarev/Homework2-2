# 1

# Обьявить строку:
s = 'dffsfsdfs'

# переход на новую строку
s = 'hello \nworld'

# интраполяция вывода
# при format мы можем указать порядок вывод в скобках!!!
print(a, ' – ', b, ' – ', s)
print('{} – {} – {}'.format(a, b, s))
print(f'{a} – {b} – {s}')
print(f'{len(number)} len')

# Обьявление массива
list = [1, 2, 3]
col = ['1', '2', '3', 'hello']
tex = ['1', '2', '3', 'hello', 1, 2, 3, 4.5, True]
print(list)
print(col)
print(tex)

# примеры вывода и ввода
print  # вывод
input  # ввод

print('введите a')       # Если мы хотим целый числовой тип данных пишем int (input()), если с плавующий точкой   float (input())
a = input()
print('введите b')
b = input()
print('{} {}'.format(a, b))  # 1 способ вывода
print(f'{a} {b}')  # 2 способ вывода

# Так же можно сложить все в ответе
print(a, '+', b, '=', a+b)

# Унаргый минус и Унаргый плюс
a = +123
b = -321
c = a+b
print(c)

# Округление по мат правилам до нужного знаков после запятой.
a = 1.3123
b = 3
с = round(a * b, 3)

# Логические операторы
 
# in - в
# or - или
# Not - нет
# is - является
                                              
f = 1 > 2 or 4 < 6                                       
f = [1, 2, 3, 4]
print(2 in f)
                                                
f = [1, 2, 3, 4]
print(not 2 in f)
                                            
is_odd = f[0] % 2 == 0
print(is_odd)

# Оператор if и else
a = int(input('a = '))
a = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

# Оператор if и if-else
username = input('Введите имя: ')
if username == 'Маша':
    print('Урра это Маша!')
elif username == 'Ильнар':
    print('Ильнар - топ')
elif username == 'Марина':
    print('Марина')
else:
    print('Привет,', username)


# Циклы while --------------------------------
a = 23
b = 0
while a != 0:
    b = b * 10 + (a % 10)
    a = a // 10
print(a)

# Циклы while c else
a = 23
b = 0
while a != 0:
    b = b * 10 + (a % 10)
    a = a // 10
    print(a)

else:
    print('тогда это!!!')

# Циклы for -------------------------------------
for i in 1, 2, 3, 4, 5:
    print(i**2)
# ---------------------------------
list = [1, 2, 3, 4, 5, 10, 8, 6]
for i in list:
    print(i)
# ---------------------------------
a = range(10)
for i in a:
    print(i)
# ---------------------------------
for i in range(5):
    print(i)
# ---------------------------------
for i in range(5):
    print(i)
# ---------------------------------
for i in 'dsd - sdsd':
    print(i)

# Строки это мосив символов и мы обрашаемся к ниму через индекс начиная с 0
text = 'Привет Васек, как ты?'
print(text[0])
print(text[-1])  # это последний символ начинаеться отчет с конца -1-2-3-4-5
print(text[:])  # напечатает весь текст
print(text[0:5])  # напечатает от 0 до 5 символа
print(text[0:-18])  # можно так указать
# ---------------------------------
numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

# ---------------------------------
ran = range(1, 6)
print(ran)

# ---------------------------------
numbers[0] = 10
print(f'{len(numbers)}')  # len это функция для получения количество элементов массива
print(numbers)

# ---------------------------------
numbers[0] = 10
for i in numbers:
    i = i * 2
    print(numbers)

# функция append - добавляет в масив символы
# функция remove - удаляет из массива символы 
colors = 'sfsdffsdffd'
colors.append('dffd') # добавить в конец
colors.remove('dffd') # удалить элемент

# Или просто передать, что хотим удалить в таком виде
del colors[0]

# Как описываються функции в пайтон
def asss(x):
    if х == 1:
     return 'целое'
    elif х == 2.3:
        return 23
    else:
        return
