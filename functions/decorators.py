# '============Функция высшего порядка======='
# # функция высшего порядка - это функция которая принимает в аргументы друую функция, создает внутри себя другую функцию , вызывает функцию и возврощает функцию.

# def func1():
#     return 'hi'

# def func2(func_):
#     print(func_())

# func2(func1)

# '==========Декораторы=========='
# # декораторы - это функции высшего порядка , которая нужна для расширения функционала другой функции не изменяя ее (функция оберток)

# def decorator_glushitel(func):
#     def wrapper (*args, **kwargs):
#         text = func(*args, **kwargs)
#         res ='тихо '+text
#         print(res)
#     return wrapper
    
# def gun():
#     print('срелять')

# wrapper = decorator_glushitel(gun)
# wrapper()#способ использоват декоратор в ручную

# def decorator_glushitel(func):
#     def wrapper (*args, **kwargs):
#         text = func(*args, **kwargs)
#         res ='тихо '+text
#         print(res)
#     return wrapper

# @decorator_glushitel   
# def gun():
#     return'срелять'

# gun()# способ использовать декоратор при помощи чинтаксического сахара

'-----------------------------------'
from datetime import datetime

# def decorator(func):
#     def wrapper():
#         print('start:',datetime.now())
#         func()
#         print('finish:', datetime.now())
#     return wrapper

# def hello():
#     print('hello world')

# wrapper = decorator(hello)
# wrapper()

'---------------------------------------------------------'

# def func_start_time(func):
#     def wrapper(*args,**kwargs):
#         print('start:',datetime.now())
#         func(*args,**kwargs)
#     return wrapper

# @func_start_time
# def sum_(a,b):
#     print(a+b)

# sum_(20,10)
'--------------------------------------------------------------'

# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 func(*args,**kwargs)
#         return wrapper
#     return inner_decorator

# @decorator(10)
# def hello():
#     print('hello world')

# hello()
'-----------------------------------------------------------------'

# colors1 = ["red", "orange", "green", "blue", "white"] 
# colors2 = ["black", "yellow", "green", "blue"] 
# resc1=[] 
# resc2=[] 
# for i in colors1: 
#     if not i in colors2: 
#         resc1.append(i) 
#         for k in colors2: 
#             if not k in colors1: 
#                 resc2.append(k) 
# print(resc1, resc2)

