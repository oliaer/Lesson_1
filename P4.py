print('Задача 1')
from sys import argv

script_name, chasy, stavka, premia = argv

z = float(chasy) * float(stavka) + float(premia)
print("Человек заработал: ", z)

print('Задача 2')
a = [1, 22, 33, 5, 6]
answer = [a for i in range(len(a) - 1) if a[i] < a[i + 1]]
print(answer)

print('Задача 3')
a = []
answer = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(answer)

print('Задача 4')
import collections
c = collections.Counter()

my_words = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

for word in my_words:
    c[word] += 1
zz = dict(c.most_common())
my_list = [key for key, val in zz.items() if val == 1]
print(my_list)

print('Задача 5')
from functools import reduce
list = [el for el in range(100, 1000, 2)]
def proizv(prev_el, el):
    return prev_el * el
print(reduce(proizv, list))

print('Задача 6_1')
from sys import argv

script_name, min_chislo = argv
from itertools import count
for el in count(int(min_chislo)):
    if el > 20:
        break
    else:
        print(el)


print('Задача 6_1')
from sys import argv

script_name, povt = argv
from itertools import cycle

с = 0
for el in cycle("ABC"):
    if с > int(povt):
        break
    print(el)
    с += 1



print("Задача 7")

def fact(n):
    f = 1
    for i in range(1, n+1, 1):
        f *= i
        yield f

n = int(input("Факториал чего будем искать? "))
for el in fact(n):
    print(el)