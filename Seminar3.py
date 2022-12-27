# 1№ Задайет списк, напишите программу которая опредилит присутствует ли в заданном списке строк некое число.

# ПРИМЕР 1№ 

# text = ['jKFJKDfdfdsm', 'dfsfsdf78fsdf','fg', 'fdfdsml18', '78']
# search = 'sm'

# for i in range(len(text)):
#     if search in text[i]:
#         print(f'Подстрока встречаеться в искомом списке на индексе: {i}')


# ПРИМЕР 2№ 

# text = ['jKFJKDfdfdsm', 'dfsfsdf78fsdf','fg', 'fdfdsml18', '78']
# search = 'sm'

# for i in text:
#     if search in i:
#         print(f'Подстрока встречаеться в искомом списке!')
#         break
#     else:
#         print('Подстрока всписке не встречаеться!')    
#         break

# ПРИМЕР 3№ 
# text = ['jKFJKDfdfdsm', 'dfsfsdf78fsdf','fg', 'fdfdsml18', '78']
# search = 'sm'

# print(text[0].find(search))



# 2№ наишите программу, которая определит позицию второго вхождени строки в списке либо сообщит, что её нет.

my_List = ['fsd', 'lklp', '123', 'qeqec', 'lnlnk', '123', 'ceet0', 'fsd']

n = '123'
count = 0

for i in range(len(my_List)):
    if (n == my_List[i]):
        count += 1
        if count == 2:
            print(i)