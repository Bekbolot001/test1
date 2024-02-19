'=======Функция======'
# функция это именнованный блок кода, который может принимать аргументы и возвращать результат.

#def get_sum(x,y): # x, y - это параметры.
#    result = x + y
#    return result

#print(get_sum(10,20))# 10, 20 - это аргументы.

"функции соблюдают принцип DRY(don't repeat yoursef)"

'========аргументы и параметры========='
# параметры переменные внутри функции задаются при создании функции
# аргументы это значение которые мы передаем при вызове функции
'=========виды параметров==========='
# 1.обезательные
# 2.не обезательные # с дефолтом (со значением по умолчанию)
                    #  args(все позиционные агументы)
                    # kwargs(все лишние именнованные аргументы).

#def func(*args, **kwargs):
#    print(args)
#    print(kwargs)

#print(func(1,2,3,'hi', hello='hello world'))

'========Выды аргументов============'
# 1. позиционные (по позиции)
# 2. именнованные (по названию(параметр = значение))

'----------------------------------------------------'
#num :int = 15
#name :str='vidmvmv'

#def sum_(a:int,b:int):
#    return a+b

#print(sum_(10,3))

#def calc_():
#    try: 
#        num1 = float(input('Enter number:'))
#        num2 = float(input('Enter number:'))
#        oper = input('Enter oper:')
#        if oper =='+':
#            print(num1+num2)
#        elif oper =='-':
#            print(num1-num2)
#        elif oper =='*':
#            print(num1*num2)
#        elif oper =='/':
#            print(num1/num2)
#        elif oper =='**':
#            print(num1**num2)
#        else:
#            raise KeyError
#    except KeyError:
#        print('вы ввели не ту операцию')
#
#     except ValueError:
#        print('ввдите число ане символы')
#    except ZeroDivisionError:
#        print('нелза делить на ноль')
    
#calc_()

db = [
    {'name':'Tima','password':hash('289138848')},
    {'name':'Nick','password2':hash('289138849')}
]

def in_database(name):
    for user in db:
        if name == user['name']:
            return True
    return False

def register(name,password,password2):
    if in_database(name):
        raise Exception('Юзер с такоим именем уже существует')
    if password != password2:
        raise Exception('Парлои не совподают')
    user = {'name':name,'password':hash(password)}
    db.append(user)
    return'Вы успешно зарегестрировались'

def login(name, password):
    if not in_database(name):
        raise Exception('Пользователь не найден!')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception('Пароль не верный')

    return 'Вы успешно залогинулись'

print(register('katana','11231233','11231233'))
print(db)
print(login('katana', '11231233'))
'-------------Lambda-------------'
# lambda - анонимная функция , которая записывается в одну строку.

#def sum_1(x,y):
#    return x + y

#sum_1(10,29)
#sum_1(1,5)
#sum_1(20,1)

#sum_2 = lambda x, y: x +y 
#print(sum_2(10,5))