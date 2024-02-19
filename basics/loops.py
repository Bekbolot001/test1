'=============Циклы========='
# циклы - это блок кода который отрабатывает несколько раз

"""Итерируемый обьект - это какая-то последовательность, которую мы можем перебрать. Например: 
[1,2,3] - list
"hello world"- ste
{'a':1,'b':2} - dict
(1,2,3,4,123,True)- tuple"""

"""Итерация - процесс перебора итерируемого обьекта"""

# 1. for - цикл который работает с итерируемым обьектом, цикл заканчивае свою работу ,когда он доходит до последнего элемента итерируемого обьекта.

# 2. while - цикл, который работает до тех пор пока условие верное.
#'FOR'
#list_ = [1,True, 'hello',0,123]
#for elem in list_:
#    if not elem == 0:
#        print(elem)

'WHILE'
#count = 0
#while count < 10:
#    print(count)
#    count = count+1

'========Кючевые слова в циклах========'
# break - оператор, который останавливает работу цикла(ломает)
# continue - оператор , который пропускает итерацию (продолжает с другой итерации)
# range(start, end, step) - генератор последовательности , от start до end(не включительно).

#print(list(range(1,11)))

#for i in range(0,21):
#    if i == 10:
#        continue
#    print(i)

#for i in ['1','2','3','hello world']:
#    if i.isdigit():
#        print(int(i))
#        print('Все хорошо')
#    elif i.isalpha(()):
#        print('я не могу перевес буквы в число')
#        break
#    else:
#        print('Я нашел символы!')

#count = 0
#passw = input('Введите пароль: ')
#while True:
#    print(count)
#    if str(count) == passw :
#        print('Введите пароль:',passw)
#        break
#    count += 1 # count = count + 11

#count = 0 
#while True:
#    if count != 0:
#        continue
#    if count == 1:
#        break
#    print(count)
#    count += 1

#else в цикле работает тогда когда условие цикла становится False, если же сработал break, то else не работает.

string ='456456' 
if ((string[0] + string[1] + string[2]) == (string[3] + string[4] + string[5])):
    print('да')
else:
    print('нет')
