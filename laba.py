# 9.1
# print('Введите число книг домашней библиотеки')
# home = set()
# m = int(input())
# print('Введите число книг в списке на лето')
# summer = set()
# n = int(input())
# for i in range(m):
#     print('Введите названия книг из домашней библиотеки')
#     bookH = input()
#     home.add(bookH)
# for i in range(n):
#     print('Введите названия книг из списка на лето')
#     bookS = input()
#     summer.add(bookS)
#     if bookS in home:
#         print('YES')
#     else:
#         print('NO')


# 9.3
# import collections
# print('Введите количество сотрудников организации')
# n = int(input())
# print('Введите их фамилии')
# last_name = []
# res = 0
# for i in range(n):
#     last_name.append(input())
# c = collections.Counter(last_name)
# for i in range(n):
#     if c[last_name[i]] > 1:
#         res += 1
# print(res)


# 10.3
# print('Введите строку')
# line = input()
# if line[0].isupper():
#     print('ДА')
# else:
#     print('НЕТ')


# 10.4
# print('Введите строку')
# line = input()
# print(line[-1])


# 11.2
# print('Введите количество строк, подлежащих обработке')
# n = int(input())
# print('Введите строки')
# for i in range(n):
#     line = input()
#     if line.startswith('%%'):
#         print(line[2:])
#     elif not line.startswith('####'):
#         print(line)


# 11.5
# print('Введите строку')
# line = input()
# while len(line) > 0:
#     print(line)
#     line = line[1:-1]


# 12.1
# print('Введите колво пунктов белого списка')
# n = int(input())
# print('Введите пункты белого списка')
# sp = [input() for _ in range(n)]
# print('Введите колво запросов, которые нужно проанализировать')
# m = int(input())
# print('Введите сами запросы')
# sp1 = [input() for _ in range(m)]
# print('Запросы, которые есть в белом списке')
# for i in range(m):
#     if sp1[i] in sp:
#         print(sp1[i])


# 12.3
# print('Введите колво покупок')
# n = int(input())
# print('Введите список покупок и сколько товара нужно купить')
# sp = []
# m = []
# for i in range(n):
#     sp.append(input())
#     m.append(input())
# for i in range(1, len(sp)+1):
#     print(sp[-i], m[-i])


# 13.2
# print('Введите колво чисел')
# n = int(input())
# print('Введите числа')
# sp = [int(input()) for i in range(n)]
# sp.sort(reverse=True)
# print('Числа в порядке убывания')
# for i in range(n):
#     print(sp[i])


# 13.4
# print('Введите колво показателей')
# s = int(input())
# print('Введите целые числа - уровень показателей каждого из братьев')
# first = [int(input()) for i in range(s)]
# second = first[:]
# print('Введите  колво тренировок')
# n = int(input())
# for i in range(n):
#     print('Введите 1 или 2 - какой из братьев тренировался')
#     brother = int(input())
#     if brother == 1:
#         print('Введите номер показателя, над которым шла работа')
#         indicator1 = int(input())
#         print('Введите на какую величину увеличился показатель')
#         value1 = int(input())
#         first[indicator1] += value1
#     elif brother == 2:
#         print('Введите номер показателя, над которым шла работа')
#         indicator2 = int(input())
#         print('Введите на какую величину увеличился показатель')
#         value2 = int(input())
#         second[indicator2] += value2
# print('Значения показателей 1 брата')
# print(*first)
# print('Значения показателей 2 брата')
# print(*second)
# k = 0
# for i in range(len(first)):
#     if first[i] == second[i]:
#         k += 1
# print('Количество совпадений между братьями')
# print(k)


# 14.1
# print('Введите колво пунктов рецепта')
# n = int(input())
# print('Введите пункты рецепта')
# recipe = [input() for i in range(n)]
# onion = []
# for i in range(n):
#     if 'лук' not in recipe[i]:
#         onion.append(recipe[i])
# print('Рецепт без лука')
# print(', '.join(onion))


# 14.3
# print('Введите строку')
# line = input()
# print(line.replace(' ', '\n'))


# 15.1
# print('Введите одну строчную букву')
# letter = input()
# print('Введите строку')
# line = input()
# for i in line.split():
#     if letter in i.lower():
#         print(i)


# 15.2
# print('Введите строку')
# line = input()
# k = 0
# for i in range(len(line)):
#     if line[i].isalnum():
#         k += 1
# print(k)


# 16.2
# print('Введите число рядов таблицы')
# R = int(input())
# print('Введите строки этой таблицы')
# rows = [input().split(',') for _ in range(R)]
# print('Введите число элементов таблицы, которые надо вывести')
# n = int(input())
# print('Введите разделенные запятой координаты элементов таблицы(строка, столбец)')
# for j in range(n):
#     row_number, column_number = [int(i) for i in input().split(',')]
#     print(rows[row_number][column_number])


# 16.3
# print('Введите размер квадратного поля(>=3)')
# n = int(input())
# print('Введите числа, описывающие колво бактерий в каждой клетке')
# description = [[int(input()) for i in range(n)] for j in range(n)]
# print('Введите колво капель антибиотика')
# k = int(input())
# for i in range(k):
#     print('Введите столбец, куда попала капля')
#     y0 = int(input())
#     print('Введите ряд, куда попала капля')
#     x0 = int(input())
#     for x in range(n):
#         for y in range(n):
#             if x0 == x and y0 == y:
#                 description[x][y] -= 8
#             elif (x == x0 - 1 and y == y0) or (x == x0 + 1 and y == y0) or (y == y0 - 1 and x == x0) \
#                     or (y == y0 + 1 and x == x0):
#                 description[x][y] -= 4
#             elif (x == x0 - 1 and y == y0 - 1) or (x == x0 - 1 and y == y0 + 1) \
#                     or (x == x0 + 1 and y == y0 - 1) or (x == x0 + 1 and y == y0 + 1):
#                 description[x][y] -= 4
# for x0 in range(n):
#     for y0 in range(n):
#         if description[x0][y0] < 0:
#             description[x0][y0] = 0
# print('Колво бактерий, выживших в каждой клетке')
# for i in description:
#     print(*i)


# 17.1
# dictionary = {'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
#               'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e',
#               'Ё': 'E', 'ё': 'e', 'Ж': 'Zh', 'ж': 'zh', 'З': 'Z', 'з': 'z',
#               'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k', 'Л': 'L',
#               'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o',
#               'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's', 'Т': 'T', 'т': 't',
#               'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х' :'kh', 'Ц': 'Tc', 'ц': 'tc',
#               'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch', 'Ы': 'Y',
#               'ы': 'y', 'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia', 'ь': '', 'ъ': ''}
# print('Введите строку')
# line = input()
# res = ''
# for i in range(len(line)):
#     text = dictionary.get(line[i], line[i])
#     res += text
# print('Транслитерированный текст')
# print(res)


# 17.2
# dictionary = {}
# print('Введите колво номеров телефонов')
# n = int(input())
# print('Введите через пробел: телефон, имя(состоит из русских букв)')
#
# for _ in range(n):
#     number, name = input().split()
#     if name in dictionary:
#         dictionary[name].append(number)
#     else:
#         dictionary[name] = [number]
# print('Введите колво запросов')
# m = int(input())
# print('Введите сами запросы(имя друга)')
# for _ in range(m):
#     request = input()
#     print(*dictionary.get(request, ['Нет в телефонной книге']))
