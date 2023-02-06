# №1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
### Пример:
### - 6782 -> 23
### - 0,56 -> 11

### Решение:
``` bash
summ = 0
Number = input('Введите число: ')

for i in Number:
    if i.isdigit():
        summ += int(i)
print('Cумму цифр:',summ)
```

## №2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Решение:

``` bash
Number = int(input('Введите число: '))
summ = 1
i = 1
while i <= Number:
    summ *= i
    i+= 1         
print(summ)    
```
# №3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму. 1+1/n**n

# Решение:
``` bash
n = int(input('Введите число: '))
my_list = []
for i in range(1, n + 1):
    consistent = round((1+1/i)**i, 1) 
    my_list.append(consistent)
print(f'Последовательность: {my_list}')
print(f'Сумма: {round(sum(my_list), 1)}')
```


