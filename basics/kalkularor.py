num1 = int(input('число1 :'))
oper = input('oper :')
num2 = int(input('число2 :'))

if num1==0  or num2==0:
    print('Тебя что в школе не учили')
elif oper == '+':
    print(num1+num2)
elif oper == '-':
    print(num1-num2)
elif oper == '*':
    print(num1*num2)
elif oper == '/':
    print(num1/num2)
elif oper == '//':
    print(num1//num2)
elif oper == '%':
    print(num1%num2)
elif oper == '**':
    print(num1**num2)
else:
    print('Это ваще не правильно')