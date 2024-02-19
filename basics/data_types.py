'==================Переменные========================='
"Переменные - это ссылки на ячейки памяти , где хронятся какие-то данные. Для дальнейшего использования" 

#name = 'Tima'
#age = 25

#num1 = 15
#num2 = 20
#print(num1+num2)
#print('Hello world')

'=================Правило наименование переменных========================'

a = 'tima' # можно, но назначение не понятно
# 1num= 12 - нельза начинать пермеменные с чисел
# num-df =13 - нельза использавать символы кроме '_'
# hello world = hello world - нельза исползавать пробелы в названии переменной
# print = 'print' - нельза называть переменнные встроиными словами из питона

# Snake case - python стиль наименнываиния переменных
my_name = 'katana'

# Camel case - стиль остальных языков программированя
MyName = 'katana'

'=================Ввод и вывод данных============================='
# print() - функция для вывода данных в терминал
# input() - функция для ввода данных с терминала

#print('makers')

#num1 = int(input('введите первое число: '))
#num2 = int(input('введите второе число: '))

#clear
#print(num1 * num2)

'============Типы данных================='
# Тиипы данных деляться на 2 вида: Изменяемые и не изменяемые 

#Изменяемые типы данных:
list_ = [1,2,3,'makers', True]
dict_ = {'a':1, 'b':12, 'c':0}
set_ = {1, 2, 13, 10, True, 'hello', False}
#Неизменяемые типы данных:
int_ = 15
float_ = 0.5
complex_ = 5j
decimal_ = 0.665765657
str_ = 'makers bootcamp'
tuple_ = (1, 2, 123, 0, -5)
boolean_1 = True
boolean_2 = False
none_type = None

#print(tuple_)
#print(int_)
#print(dict_)


#name = 'Tima'
#age = 25

num1 = 10
num2 = 5

print(num1 + num2) #сложение = 15
print(num1 - num2) #вычитание = 5
print(num1 * num2) #усножение = 50
print(num1 / num2) #дробное деление = 2.0
print(num1 // num2) #целочисленное деление = 2
print(num1 % num2) #деление по остатку= 0
print(num2 ** num2) #возведение в степень = 100000
print(num1 ** 0.5) #корень числа
from math import sqrt
print(sqrt(num1)) #корень числа
print(abs(-num1)) # |-10| -> 10 модуль числа
print(round(5.6)) # 6 (округление в большую сторону)
print(round(5.5)) # 6
print(round(5.4)) # 5 (округление в сторону меньше)
print(round(5.49)) # 5
print(pow(2, 3)) # 2 ** 3 = 8
print(pow(2, 3, 4)) # (2 ** 3) % 4 = 0
print(divmod(5, 2)) # 2, 1 | (5 // 2) % 2 = 0
# divmod - это функция ктотрая возвращает 2 числа:
# 1 число это - целочисленное деление 
# 2 число это - деление по остатку
divmod(17/ 3)
#1 действие 17 // 3 = 5
#2 действие 17 % 3 = 2