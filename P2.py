print("Задача 1")
result_list = [2, 'text', 456, 45.3, None, False]
for l in result_list:
    print(type(l))

print("Задача 2")
symbols = list(input("Вводи список и ни в чем себе не отказывай "))
list=[]
i = -2

if len(symbols) // 2 != 0:
    symbols.append('testhren')
for el in range(len(symbols)):
    i=i+2
    if i<len(symbols)-1:
        list.append(symbols[i+1])
        list.append(symbols[i])
myString = ''.join(list)
myString=myString.replace('testhren', "")
print(myString)


print("Задача 3")
str=input()
zz=(str.split())
for el in enumerate(zz):
    print("Номер строки: ", el[0:10])

print("Задача 4_1")
nomer_mes = int(input("Введи же номер месяца сейчас же: "))
seasons=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if nomer_mes in seasons[0:2]:
    print("Зима", nomer_mes)
elif nomer_mes in seasons[3:5]:
    print("Весна", nomer_mes)
elif nomer_mes in seasons[6:8]:
    print("Лето", nomer_mes)
elif nomer_mes in seasons[9:11]:
    print("Осень", nomer_mes)

print("Задача 4_2")
mes = {"Зима": [1, 2, 3], "Весна": [4, 5, 6], "Лето": [7, 8, 8], "Осень": [10, 11, 12]}
search_age = int(input("Введи же номер месяца сейчас же: "))
for kluc, [x, y, z] in mes.items():
    if x == search_age or y == search_age or z == search_age:
        print(kluc)


print("Задача 5")
my_list = [7, 5, 3, 3, 2]
el = int(input("Введите элемент: "))
my_list.append(el)
item = sorted(my_list)
print(item[::-1])


print("Задача 6")
col_vo = int(input("Введите количество товара "))
n = 1
result_list_nazv = []
result_list_cena = []
result_list_kol = []
result_list_ed = []
result_list_keys = []
while n <= col_vo:
    n += 1
    my_dict = dict({'Название': input("Название "), 'Цена': input("Цена "), 'Количество': input("Количество "), 'Единицы': input("Единицы ")})
    for key, el in my_dict.items():
        result_list_keys.append(key)
        if key == 'Название':
            result_list_nazv.append(el)
        if key == 'Цена':
            result_list_cena.append(el)
        if key == 'Количество':
            result_list_kol.append(el)
        if key == 'Единицы':
            result_list_ed.append(el)
print(result_list_keys[0], result_list_nazv)
print(result_list_keys[1], result_list_cena)
print(result_list_keys[2], result_list_kol)
print(result_list_keys[3], result_list_ed)

