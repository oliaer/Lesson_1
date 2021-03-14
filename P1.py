print("Задача 2")
ttime = int(input("Введи число, амиго: "))
sec = (ttime % 60) #эта фигня считает секунды
minutes = (ttime-sec)/60
minutes_full = (minutes % 60)
hour = (minutes // 60)
print("%.0f" % hour, ":", "%.0f" % minutes_full, ":", sec)


print("Задача 3")
chislo1 = int(input("Введи число, амиго: "))
rezult4 = int(chislo1) + int(str(chislo1) + str(chislo1))+int(str(chislo1) + str(chislo1) + str(chislo1))
print(rezult4)

print("Задача 4")
chislo = int(input("Введи число, амиго: "))
ostatok = chislo % 10
chislo = chislo // 10
while chislo > 0:
    if chislo % 10 > ostatok:
        ostatok = chislo % 10
    chislo = chislo//10
print(ostatok)


print("Задача 5")
prib=int(input("Какая прибыль? "))
izd=int(input("Какие издержки? "))

if prib>izd:
    print("Это успех, рентабельность: ", "%.2f" % (prib/(prib-izd)))
else:
    print("Идите работать, ленивые клячи")

sotr=int(input("Сколько сотрудников? "))
print("Прибыль на сотрудника: " "%.2f" % (prib/sotr))

print("Задача 6")
a = int(input("С чего начал? "))
b = int(input("Какая великая цель? "))
dni = 1
rasst = a

while rasst < b:
    dni=dni+1
    rasst=rasst+0.1*rasst
    print("День", dni, "Расстояние", "%.3f" % rasst)
print("Это будет",  dni, "дней")

