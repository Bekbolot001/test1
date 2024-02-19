'========Области видимости========'
#LEGB - Local enclosed global build-in

'=====Build-in======='
# встроенное пространство имен(list, print, dict, len, input)

'=============Global========='
# все прменные , которые мы создали внутри файла 
#чтобы посмотреть все глобальгые переменные ,можно использовать функцию global
a = 10
b = 'hello'
print(globals())

'=======enclosed======='
#замкнутое пространство имен - это локальное пространство , у которого есть внутреннее локальное пространство

var = 'global' # хранится в глобальном пространстве

def func():
    var = 'enlosed' # замкнутое
    def inner_func():
        var = 'local' # локальное
        print(var)# local
    print(var)# enclosed
    inner_func()
print(var) # global
func()

'========Local=========='
# локальное пространство имен - это пространство которое находится внутри функции 

#a = 10 
#def func(a,b):
#    res = a + b
#    print(res)
#    print(locals())
#    print(globals())

#func()

#def count_():
#    count = 0
#    def inner_count_():
#        count+=1
#        print(count)
#    inner_count_()

#count_

#def count_(num):
#    count = 0
#    def inner_count_():
#        nonlocal count
#        count+=1
#        print(count)
#    for i in range(num): 
#        inner_count_()

#count_(12)

