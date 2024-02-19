'===========comprehensions========='
#генератор, с помощью которого мы можем создавать последовательности использу цикл for в одну строку.

# элемент for элемент in последовательность 
# элкмент for элемент in последовательностьif фильтр 

# элемент1 if условие1 else элемент2 for элемент in последовательность

#compr_ = [i for i in range(6)] 
#print(compr_)

#compr_1 = []
#for i in range (6):
#    compr_1.append(i)
#print(compr_1)

#compr_ = [i if i % 2 == 0 else 'elem' for i in range(10)] 
#print(compr_)

#compr_1 = []
#for i in range (10):
#    if i % 2 == 0:
#        compr_1.append(i)
#    else:
#        compr_1.append('elem')
#print(compr_1)

#compr_1 = []
#for i in range (10):
#    if i % 2 == 0:
#        compr_1.append(i)
#print(compr_1) # [0,2,4,6,8]

'создайте новый лист использу старый . В новом лисе должно быть только True значение'
#list_ = [12, None, 'hi', 123,1,6,2,True,0,False]

#new_list_ = [i for i in list_ if bool(i)]
#print(new_list_)

#new_list_2 = [ i if bool(i) else 0 for i in list_]
#print(new_list_2)

#new_list_2 = []
#for i in list_:
#    if bool(i):
#        new_list_2.append(i)
#    else:
#        new_list_2.append(0)
#print(new_list_2)

'============Виды comprehensions==============='

#list comprehensions -> []
#dict comprehensions -> {:}
#set comprehensions -> {}

# comprehension генератор -> ()
# compr_ = (i for i in range(11))
# print(compr_)

'DICT comprehensions'

# {1:1,2:4,3:9,4:16}

#dict_ = {i:i**2 for i in range(1,5)}
#print(dict_)

#dict_ = {'a':1, 'b':2,'c':3}
#new_dict_ = {v:k for k,v in dict_.items()}
#print(new_dict_)

#new_dict_2 = { v**2:2 for v in dict_.values()}
#print(new_dict_2)

'SET_COMPREHENSHION'
#set_ = {i for i in range(11) if i % 2 == 0}
#print(set_)

#set_1= {12, 34, 1, 'hi', 'hello', 123, None}
#print(set_1)
#set2= {i.swapcase() for i in set_1 if type(i)==str}
#print(set2)

'=================Вложенные comprehensions==============='

# Создайте словарь, где ключами будут число от 1 до 5 , а значениями - списки от 1 до этого числа
#dict_= {}
#for i in range(1,6):
#    key = i
#    values = [j for j in range(1, i+1)]
#    dict_[key] = values

#dict_ = {i :[j for j in range(1, i+1)] for i in range(1,6)}
#print(dict_)

