'==============JSON=========='
# JavaScript Object Notation - универсальный формат, в котором мы сожем хранить данные в типах и данных , понятных почти для всех языков программирования 

# import json
# json_data = "null"
# python_data = json.loads(json_data)
# print(python_data)

# with open('test.json', 'r') as file:
#     python_data = json.load(file)

# print(python_data)

# десериализация - перевод с json строки в python обьекты
# loads - метод для десерализации с json строку
# load - метод для десерализации с json файла

# сериализация - перевод python обьектов в json строку
# dumps - метод для серализации с json строку
# dump - метод для серализации с json файла
import json
python_data  = None
json_data = json.dumps(python_data)
print(json_data)

with open('test_json', 'w') as file:
    json.dump(json_data,file)

python_data = [1,2,True,False,None,'makers']
