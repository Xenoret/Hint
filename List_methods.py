#!usr/bin/env python
#! -*- coding: utf-8 -*-

#Методы списков

import os

os.system('cls||clear') #Use for clear terminal
print('\nВ Python у списков имеется одиннадцать методов. Большинство из них предназначены для вставки и удаления элементов.\n')
#Меню выбора
met = ''' 
1 - append() - добавляет элемент в конец списка.
2 - clear() - удаляет все элементы из списка
3 - copy() - делает поверхностную копию списка
4 - count() - считает, сколько раз в списке встречается переданный аргумент
5 - extend() - добавляет в конец списка итерируемую последовательность.
6 - index() - возвращает индекс указанного элемента.
7 - insert() - вставляет элемент перед указанным индексом.
8 - pop() - удаляет элемент по указанному индексу и возвращает его. 
9 - remove() - удаляет первый объект из списка, значение которого равно аргументу.
10 - reverse() - переворачивает список на месте.
11 - sort() - сортировка списка на месте (список изменяется, а не возвращается новый).
00 - Выход\n
'''

one = '''
	append() - добавляет элемент в конец списка. 

	>>> lst = ['a', 45, 89, 'who']
	>>> lst.append(67)
	>>> lst
	['a', 45, 89, 'who', 67]\n '''

two = '''
	clear() - удаляет все элементы из списка

	>>> a = [1,2]
	>>> a.clear()
	>>> a
	[] \n'''

three = '''
	copy() - делает поверхностную копию списка

	>>> a = [1, 2]
	>>> b = a.copy()
	>>> b.append(3)
	>>> a
	[1, 2]
	>>> b
	[1, 2, 3]
	 
	>>> c = [1, 2, [3, 4]]
	>>> d = c.copy()
	>>> d.append(5)
	>>> c[2].append(6)
	>>> c
	[1, 2, [3, 4, 6]]
	>>> d
	[1, 2, [3, 4, 6], 5] \n'''

four  	= 	''' 
	count() - считает, сколько раз в списке встречается переданный аргумент.

	>>> a = [1, 0, 1, 1, 0]
	>>> a.count(1)
	3 \n'''

five	= 	''' 
	extend() - добавляет в конец списка итерируемую последовательность.

	>>> b
	[1, 2, 3]
	>>> c = (9, 10)
	>>> b.extend(c)
	>>> b
	[1, 2, 3, 9, 10]
	>>> b.extend("abc")
	>>> b
	[1, 2, 3, 9, 10, 'a', 'b', 'c']
	>>> b.extend([12, 19])
	>>> b
	[1, 2, 3, 9, 10, 'a', 'b', 'c', 12, 19] \n'''

six 	= 	''' 
	index() - возвращает индекс указанного элемента. Если таких элементов несколько, вернет индекс только первого. 
	Eсли таких элементов нет,генерируется исключение. Вторым и третьим аргументом можно указать срез для поиска. 

	>>> a = ['a', 'c', 'e', 'a', 'b']
	>>> a.index('a')
	0
	>>> a.index('a', 2)
	3
	>>> a.index('a', 2, 4)
	3
	>>> a.index('a', 2, 3)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: 'a' is not in list\n'''

seven 	= 	''' 
	insert() - вставляет элемент перед указанным индексом. Сначала передается индекс, затем элемент.

	>>> lst.insert(0,10)
	>>> lst
	[10, 'a', 45, 89, 'who', 67, 'a1', (1, 2, 3)]
	>>> lst.insert(len(lst),10)
	>>> lst
	[10, 'a', 45, 89, 'who', 67, 'a1', (1, 2, 3), 10]
	>>> lst.insert(3,10)
	>>> lst
	[10, 'a', 45, 10, 89, 'who', 67, 'a1', (1, 2, 3), 10] \n'''

eight   = 	''' 
	pop() - удаляет элемент по указанному индексу и возвращает его. Если индекс не указан, то удаляет и возвращает последний элемент. 
	Метод генерирует исключения, если список пуст или указан индекс за пределами диапазона. 

	>>> lst.pop()
	10
	>>> lst
	['a', 45, 10, 89, 'who', 67, 'a1', (1, 2, 3)]
	>>> lst.pop(1)
	45
	>>> lst
	['a', 10, 89, 'who', 67, 'a1', (1, 2, 3)]
	>>> lst.clear()
	>>> lst.pop()
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	IndexError: pop from empty list
	>>> lst.append(10)
	>>> lst.pop(2)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	IndexError: pop index out of range\n'''

nine 	= 	''' 
	remove() - удаляет первый объект из списка, значение которого равно аргументу. 
	Если такого элемента нет, то возникает ошибка.

	>>> lst.remove(10)
	>>> lst
	['a', 45, 10, 89, 'who', 67, 'a1', (1, 2, 3), 10]
	>>> lst.remove(100)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: list.remove(x): x not in list \n'''

ten 	= 	'''  
	reverse() - переворачивает список на месте.

	>>> lst
	['a', 10, 89, 'who', 67, 'a1', (1, 2, 3), 10]
	>>> lst.reverse()
	>>> lst
	[10, (1, 2, 3), 'a1', 67, 'who', 89, 10, 'a']\n'''

eleven 	= 	'''  
	sort() - сортировка списка на месте (список изменяется, а не возвращается новый).

	>>> li = [4, 1, 9, 5]
	>>> li.sort()
	>>> li
	[1, 4, 5, 9]
	>>> print (li.sort())
	None\n'''

print(met) #Вывод на экран меню
while met:
	methoods = input('Введите номер интересуещего вас пункта:\n')
	if methoods == '1':
		print(one)
	elif methoods == '2':
		print(two)
	elif methoods == '3':
		print(three)
	elif methoods == '4':
		print(four)
	elif methoods == '5':
		print(five)
	elif methoods == '6':
		print(six)
	elif methoods == '7':
		print(seven)
	elif methoods == '8':
		print(eight)
	elif methoods == '9':
		print(nine)
	elif methoods == '10':
		print(ten)
	elif methoods == '11':
		print(eleven)
	elif methoods == '00':
		print('До новых встреч!')
		os.system('cls||clear') #Стереть результат программы в терминале Windows и Linux
		exit()
	else:
		print('\n\n!!!ВНИМАНИЕ!!!   Вы ввели неизвестные мне символы, прошу повторите попытку!   !!!ВНИМАНИЕ!!!\n\n')
