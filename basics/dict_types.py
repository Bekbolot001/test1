'=================Словари==============='
# dict - изменяемый , итерируемый, неупорядоченный , неиндексируемый, тип данных, для хранение данных в парах(ключ:значение)

#user = {'name':'sultan', 'age':20, 'nick':'katana'}
#print(user['age'])# 20
#print(user['nick'])# katana
#print(user['name'])# sultan

#{ключ:значение, ключ:значение, ......}
# ключ - не изменяемый тип данных, уникальный.
#значение - дюбые: и изменяемый и не изменяемфй тип данных. Могут повторятся.

'================создание=============='
#dict1 = {'a':1,'b':2}
#dict2 = dict([('a':1),('b':2)])
#dict3 = dict(['a1','b2'])
#dict4 = {'adres',2113}
#dict4['name'] = 'tima'
#dict4['age'] = 100
#dict4['nick'] = 'collection'
#print(dict4) # {adres,2113,'name','age','nick'}

'==========Методы словарей=========='
# get - метод , котоый возвращает значение по ключу, если такого ключа нет то возвращает дефолтные значение, чаще всего None

#user = {
#    'name' : 'Nick',
#    'age' : 100,
#    'telephon_numbe':'787197398242983'
#}

#print(user['dsjbhjnd']) # keyError
#print(user.get('ggcccccgh','Нет такого ключа')) #Нет такого ключа
#print(user.get('name')) # Nick
#print(user.get('id')) # None

# pop - удаляет пару по ключу и возврашает значение
#dict_ = {'a':1,'b':2,'c':3}
#popped_values = dict_.pop('a')
#print(popped_values) # 1
#print(dict_) #{'b':2,'c':3}

# popitem - удаляет последнюю пару и возвращает ее

#dict_ = {'a':1,'b':2,'c':3}
#popped_values = dict_.popitem()
#print(popped_values) # ('c',3) 

#print(dir(dict()))

# updat - расштряет словарь парами из вторго словаря

#dict1 = {1:'a',2:'b'}
#dict2 = {3:'c',4:'d'}
#dict1.update(dict2)
#print(dict1) #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

#clear - очищает словарь
#dict_ = {1:1,2:2,3:3}
#dict_.clear()
#print(dict_)# {}

# fromkeys - метод для создания нового словаря, используя список ключей

#dict_ = dict.fromkeys([1,2])
#print(dict_) # {1:None,2:None} 

#dict_ = dict.fromkeys([1,2], True)
#print(dict_) # {1:True,2:True} 

#dict2 = dict.fromkeys('abcd',0)
#print(dict2) #{'a': 0, 'b': 0, 'c': 0, 'd': 0}

#copy , deepcopy, setdefault - самостоятельный разбор.!!!!!!!!!!!!!!!!!!!

# items - метод , который достает ((ключь,значение),(ключь,значение)...)
# vaules -  метод, который возвращает значениея

#dict_ = {'a':1,'b':2,'c':3}
#print(dict_.values())
#print(dict_.keys())
#print(dict_.items())

'=============Циклы с dict=============='
#dict_={'a':1,'b':2,'c':3}
#print(dict_['a'])
#print(dict_['b'])
#print(dict_['c'])

#dict_={'a':1,'b':2,'c':3}

#for i in dict_:
#    print(i)

#dict_ = {'a':1,'b':2,'c':3}
#dict_2 = {}
#for k, v in dict_.items():
#    dict_2[v] = k
#print(dict_2)
    
# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# dict1={}
# for k,v in dict_.items():
#     if v == None:
#         dict1.setdefault(k)
# print(dict1)

# users = [
#     {'name':'makers','age':20},
#     {'name':'anonym','age':15},
#     {'name':'sem','age':25}
# ]

# filtered = filter(lambda x: x['age'] > 18, users)
# print(list(filtered))

# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# for k in dict_.keys():
#     if k == str(k):
#         b = len(k)
#         print(max(b))

list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
dict_ = {}
for i in list_:
    if i == str():
        k = i
        if i == int():
            v = i
            dict_.setdefault(k,v)
    print(dict_)