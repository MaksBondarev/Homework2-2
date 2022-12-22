# 1. Напиши программу, которая принимает на вход два числа и проверяет, являеться ли одно число квадратом друглва.
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8, 9 -> нет

# Решение:

# import os
# def clear(): return os.system('cls')
# clear()

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# if a == b ** 2 or b == a ** 2:
#     print('Да')
# else:
#     print('Нет')


# 2. Напишите программу которя на входи принемает 5 чисел и находит максимальное из них.
# пример через max
import os
def clear(): return os.system('cls')
clear()

# my_list = []
# for i in range(5):
#     number = int(input('Введите число: '))
#     my_list.append(number)
# print(max(my_list))    

# пример ,без функции "max"
# my_list = []
# for i in range(5):
#     number = int(input(f'Введите {i + 1} число: '))
#     my_list.append(number)
#     my_max = my_list[0]

# for item in my_list:   
#     if my_max < item:
#        my_max = item
# print(f'Максимальное число: {my_max}')  
#      
# Пример 2
my_list = []
for i in range(5):
    number = int(input(f'Введите {i + 1} число: '))
    my_list.append(number)
    my_max = my_list[0]

for i in range(1, len(my_list)):   
    if my_max < my_list[i]:
       my_max = my_list[i]
print(f'Максимальное число: {my_max}')   

