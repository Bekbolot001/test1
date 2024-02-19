'==============Sting==================='
#строки - неизменяемый тип данных, который предназначен для хранения текста, заклбченного а ординарные либо двойные кавычки

string1 = 'строка с ординарными кавычками '
string2 = "строка с двойными кавычками"
# string3 = 'не правильная строка"
string4 = "Don't" # внутри двойной кавычки все ординарные - просто символы
string5 = '''       многострочный текст   в одинарных кавычках, тут можно ставить 'любые' "кавычки'    '''
string6 = 'hello' + ' ' + 'world'
#print(string6) 

string7 = 'ORE!!!' * 9
#print(string7) 
'==========Экранизация стрк================'
'\n' # переносит текст на новую строку
#print('hello\nworld')
#hello
#world

'\t' # табуляция
#print('hello\tworld')
# hello    world

str1='don\'t' # отображает кавычку 
#print(str1)
str2 = "don\"t"
#print(str2)

str3 = 'Символ -\\'
#print(str3)

'\v' # перенос на новую строку со смещением вправо на длину предыдущей строки
#print('heloo\vworl\vmakers\vbootcamp')

'\r' # перенос каретки на начало строки
#print('Makers bootcamp\rHi')
# Hikers bootcamp

'===========форматирование строк==================='

#1 
title = 'iphone14'
prise = 150
format1 = 'Мой телефон', title, 'стоит ', prise, 'долларов'
format2 = f'Мой телефон {title} стоит {prise}$'
#print(format2)

#2
#string = 'Название : {} Цена {}$'
#print(string.format('iPhon', 150))

#3
#string = 'название: %s Цена: %s'
#print(string % ('iphone', 150))

'=====================Методы строок==================='
# методы- это функции , которые относятся к определенному классу, к ним можно обращятся через точку

#print(dir(str))

string = 'hello'

#print(string.upper()) # MAKERS все большими делает
#print(string.lower()) # makers вее маленькими делает
#print(string.swapcase()) # каждую букву набарот

#print(string.title()) # helLO world-> Heloo World первые буквы большыми

#print(string.capitalize()) # hello world-> Hello world Толлько певое слово
#print(string.center(11, '-')) # '---hello---'
#print(string.count('h')) # hello -> 1 считает колсиество укзанных букв или чисел

#string = 'hello'
#print(string.startswith('a')) #False
#print(string.startswith('h')) #True
#print(string.startswith('H')) #False он смотрит с какой буквы начинается слово
#print(string.endswith('d')) # False
#print(string.endswith('lo')) #True   он смотрит с какой буквы заканчивается слово

#string = 'makers'
#print(string.islower()) # makers -> True
#print(string.islower()) # MAKERS -> False проверяет маленькте буквы

#string = 'makers'
#print(string.isupper()) #  makers -> False
#print(string.isupper()) # MAKERS -> True проверяет большие буквы

#string ='122132312'
#print(string.isdigit())# True проверяет на цифры
#print(string.isalpha())# False проверяет на буквы

#string ='122cjcjs312'
#print(string.isalnum()) #True проверяет на наличие символов

#string = 'hello world makers bootcamp'
#print(string)
#print(string.split()) #делит предложение на слова 

'==============Индексы================'
# индекс - порядковый номер элемента в последовательности (символа в строке), (ндексация начинается с 0)

'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
#               -3 -2 -1

#string = 'hello world'
#print(string[0])  # 'h'
#print(string[7])  # 'o'
#print(string[10])  # 'd'
#print(string[-1])  # 'd'

# срезы - подстрока (часть строки)
# string[start:end(не включительно):step]
#string = 'hello world'
#print(string[3:8]) # 'lo wo'
#print(string[:])  # 'hello world'
#print(string[6:])  # 'world'
#print(string[:5])  # hello

#print(string[::-1])  # 'dlrow olleh'
#print(string[::2])  # 'hlowrd'
#print(string[::3])  # 'hlwl'
#print(string[::4])  # 'hor'

#string = 'hello'
#new_string = string.upper() #hello ->HELLO
#print(new_string)

a = int(input(':'))

if a % 2 != 0:
    print('первый')
elif a % 2 == 0:
    print('второй')
else:
    print('bot true')
   