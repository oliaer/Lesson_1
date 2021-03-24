print('Задача 1')
my_file = open('task1.txt', 'w')
lines = ''
while True:
    my_file.writelines(lines + '\n')
    lines = input('Строка: ')
    if lines == '':
        break
my_file.close()

print('Задача 2')
z = ''
i = 0
with open(r"task1.txt", "r") as file:
    for line in file:
        i = i + 1
        line = line.split()
        l = len(line)
        print('В строке ', i, l, 'слов')

print('Задача 3')
salary = {}
i = 0
y = 0
with open(r"task1.txt", "r") as file:
    for line in file:
        my_list = line.strip().split()
        salary.update({my_list[0]: my_list[1]})

for key, value in salary.items():
    i = i + 1
    y = y + int(value)
    if int(value) <= 20000:
         print(key)
print('Средняя зарплата', y/i)

print('Задача 4')
sss=[]
with open(r"task4.txt", "r") as file:
    for line in file:
        line = line.replace('One', 'Один')
        line = line.replace('Two', 'Два')
        line = line.replace('Three', 'Три')
        line = line.replace('Four', 'Четыре')
        sss.append(line)
with open('task4_res.txt', 'a') as file:
     for line in sss:
         file.writelines(line)

print('Задача 5')
my_file = open('task5.txt', 'w')
lines = input('Строка: ')
my_file.writelines(lines + '\n')
my_file.close()
z = []
with open(r"task5.txt", "r") as file:
    for line in file:
        my_list = line.split()
for el in my_list:
    el = int(el)
    z.append(el)
print(sum(z))

print('Задача 6')
my_dict = []
all = {}
p=0
with open('task6.txt', 'r', encoding='UTF-8') as f:
    for line in f.read().split('\n'):
        line = line.replace(':', '').replace('—', '0').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '')
        my_dict.append(line)
    for i in my_dict:
        my_list = i.split()
        p = int(my_list[1]) + int(my_list[2]) + int(my_list[3])
        all.update({my_list[0]: p})
print(all)

print('Задача 7')
import json
dict = {}
avr = []
i=0
with open(r"task7.txt", "r") as file:
    for line in file.read().split('\n'):
        name, forma, v, iz = line.split()
        prib = int(v) - int(iz)
        if prib >= 0:
            i = i+1
            avr.append(prib)
        dict.update({name: prib})
list_firms = dict
final_list = [list_firms, {'average_profit' : sum(avr)/i}]
print(final_list)

with open("task7.json", "w") as write_f:
    json.dump(final_list, write_f)
