'========== Модули и пакеты ==========='
#.py - module,это модуль
# more modules - package

'===========File==========='
#open() - это ункция которая открываетфайл в определенном режиме

# r - read(только для чтения)
# w - write (только для записи, каждый раз файл очищается)
# a - append (только для дозаписи, добовляется в конец ) 
# x - создает файл , но если он существует то выйдет ошибка
'---------Read-----------'
# file = open('test1.txt', 'r')
# print(dir(file))
# print(file.writable())# False

# file = open('test1.txt', 'w')
# print(dir(file))
# print(file.writable())# False эмес True из за того что там 'w'

# file = open('test1.txt', 'r')

# # print(dir(file))
# # print(file.writable())# False
# # print(file.readable())# True
# # print(file.read())#read file
# # file.seek(4)
# # print(file.read())
# # print(file.read(10))
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())
# # print(file.tell())
# # print(file.readlines())
# # print(file.tell())
# file.close()
'read:str,redline:str,readlines:List[str]'

'===========Write=========='
# file = open('test1.txt','w')
# # file.write('shooooooooooooooooooooooooo\nshoooooooooooooooooooo')
# # file.writelines(['hlooo world\n','makers\n'])
# file.close()

'write(str), writelines(list[str,str])'

'=========Append==========='
# добавляет записи в конец

# file = open('test1.txt','a')
# file.write('py33\n')
# file.write('py32\n')
# file.write('py34\n')
# # file.close()

'======Констекстный менеджер========'
# with

with open('test1.txt') as f:
    print(f.read())

print(f.closed) # True - файл закрылся



