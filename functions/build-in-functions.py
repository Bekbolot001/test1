'=======Встроенные функции=========='
# map , filter, reduce, zip, enumerate.

'ZIP'
# соединяет несколько последовательностей (получаем генератор , в котором элемнты -tuple)(zip object)

# list_1 = [1,2,3,4]
# list_2 = ['a','b','c']
# list_3 = [10.5, 20.0, 1.3, 0.5]

# zipped = zip(list_1,list_2,list_3)
# print(zipped) # <zip object at 0x7f8ajs23fs>
# print(list(zipped))
# print(tuple(zipped)) # будет работать если убрать print list
# print(dict(zipped))# работает только если листов два

'ENUMRATE'
#  нумирует последовательность (по дефолту с 0),(тоже возврощвет генератор)
# <enumerate object 0x7kjf8390sjd90>

# enumerate = enumerate('hello world')
# print(enumerate)# <enumerate object 0x7kjf8390sjd90>
# # print(list(enumerate))#[(0,'h'),(1,'e'),(2,'l'),(3,'l')....]
# for elem in enumerate:
#     print(elem)

'MAP'
# ригимает функцию и последовательость 
# записывает в новую последовательность результат функции, приминив каждый элемент последовательности

# list_ = ['1','2','3','4']
# mapped = map(int , list_)
# print(list(mapped))#[1,2,3,4]

# list_ = ['1fsf','23','3ft','4g']
# mapped2 = map(str.isdigit, list_)#[flase,true,false,false]
# print(list(mapped2))

# list_ = [12,34,1,2,6]
# def pow_(x):
#     return x **2

# print(list(map(pow_, list_)))

# print(list(map(lambda x:x**2, list_)))

# str_ = 'hello world'
# mapped = map(str.upper, str_)
# print(''.join(list(mapped)))

# print(''.join(list(map(str.upper, 'hello world'))))

'FILTER'
# # возврощает генератор с элементами , прошедшими фильтрацию (какое - то условие), пригимает функцию и последовательность.

# list_ = [12,-2,0,-1,-34,38]
# filtered = filter(lambda x:x>=0, list_)
# print(list(filtered))# <filter object 0x7jdfj

# users = [
#     {'name':'makers','age':20},
#     {'name':'anonym','age':15},
#     {'name':'sem','age':25}
# ]

# filtered = filter(lambda x: x['age'] > 18, users)
# print(list(filtered))

'REDUCE'
#принимает функцию и последовательность , возврощает 1 элемент (передаваемая функция должна принимать 2 аргумента)
# импортирутся из functools

#from functools  import reduce

# list_ = [1,2,4,1,5,10]
# res  = reduce(lambda x, y: x*y, list_)
# print(res) # 300
# если тут + res  = reduce(lambda x, y: x+y, list_) то # [1241510]

# users = [
#     {'name':'makers','age':20},
#     {'name':'anonym','age':15},
#     {'name':'sem','age':25}
# ]

# from functools  import reduce

# def func(x,y):
#     if x['age'] < y ['age']:
#         return x
#     else:
#         return y
# print(reduce(func, users))

# list_ = [ 1,2,4,6,1,9,-1,6,-12]

# from functools  import reduce

# def func(x,y):
#     if x < y:
#         return x
#     else:
#         return y
# print(reduce(func, list_))

# from functools  import reduce

# res = reduce(lambda x,y: x if x<y else y, list_)
# print(res)


