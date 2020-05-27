# Наследование

import os

def clear():
	os.system('cls|clear')
clear()






print('До наследования!')

class Calc(object): #Класс родитель
	def __init__(self, number):
		self.number = number

	def calc_and_print(self):
		value = self.calc_value()
		self.print_number(value)

	def calc_value(self):#В дальнейшем будет изменён в классе наследнике
		return self.number * 10 + 2

	def print_number(self, value_to_print):
		print('-----' * 5)
		print('number is', value_to_print)
		print('-----' * 5)

c = Calc(3)
c.calc_and_print()








print('\n\n\nПосле наследования и видоизменения!')

class Calc(object):
	def __init__(self, number):
		self.number = number

	def calc_and_print(self):
		value = self.calc_value()
		self.print_number(value)

	def calc_value(self):
		return self.number * 10 + 2

	def print_number(self, value_to_print):
		print('-----' * 5)
		print('number is', value_to_print)
		print('-----' * 5)

#Производим изменение класса родителя в классе наследнике для получения иного результата, не ломая код.
class CalcExtraValue(Calc):#Класс наследник
	def calc_value(self):
		return self.number - 100

c = CalcExtraValue(3)
c.calc_and_print()

