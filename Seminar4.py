#№1 Как создать словарь и как к нему обрашаться

# my_dict = {}

# number = int(input('Введите целое число: '))

# for n in range(1, number +1):
#     my_dict[n] = 3 * n + 1
# # print(my_dict)
# print(my_dict.get(10, 'Такого ключа нет')) # если хотим обратиться к определенному ключу

#№2 Найти корень квадрата уровнения  Ax2 + Bx + C = 0 c помошью матиматической формылы нахождение карней квадратного уровнения.

import math

equation = '3 *x** 2 + 5*x - 6 = 0'

def create_koef(equation: str ):
    new_equation = equation.replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -') 
    new_equation = new_equation.split()
    new_list = []

    for i in new_equation:
        if i.startswith('x'):
            new_list.append(1)
        elif i.startswith('-x'):
            new_list.append(-1)    
        else:
            new_list.append(i.split('*x') [0])
    return new_list


def solve_equation(koef):
    a, b, c = int(koef[0]), int(koef[1]), int(koef[2])
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        x1 = (-b - math.sqrt(disc)) / (2 * a)       
        x2 = (-b + math.sqrt(disc)) / (2 * a)       
        return round(x1, 2), round(x2, 2)
    
    elif disc == 0:
        x = (-b - math.sqrt(disc)) / (2 * a)  
        return round(x, 2)
    else: 
        return None


print(solve_equation(create_koef(equation)))

