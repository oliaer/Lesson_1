print("Задача 1")
def delenie ():
    var1 = int(input("Введи первое число: "))
    var2 = int(input("Введи второе число: "))
    while var2 == 0:
        var2 = int(input("Не вводи ноль: "))
    z = var1/var2
    return z

print(delenie())

print("Задача 2")
def user_info (imja, famil, god, gorod, email, telef):
    z = (imja, famil, god, gorod, email, telef)
    return z

print(user_info('Nika', 'Pogorelova', '2017', 'Kharkov', 'nika@gmail.com', '7123456789'))

print("Задача 3")
def slog (s1, s2, s3):
    item = sorted([s1, s2, s3])
    z=item[2]+item[1]
    return z

print(slog(60, 20, 30))

print("Задача 4_1")
def stepen_1 (b1, b2):
    return b1**b2

print(stepen_1(1200, -3))

print("Задача 4_2")
def stepen_2 (b1, b2):
    i=b2*-1
    z1 = b1
    z = 2
    while z<=i:
        z=z+1
        z1=z1*b1
    return 1/z1

print(stepen_2(1200, -3))

print("Задача 5")
def summator():
    y = []
    while True:
        x = input("Введи числа, специальный символ a, для выхода zz: " )
        if x == 'zz':
            break
        ww = x.split()
        y.extend(ww)
        result_list = []
        for i in y:
            if i == 'a':
                print("Запускайте заново, последний успешный результат:")
                break
            result_list.append(i)
        result = [float(item) for item in result_list]
        print(sum(result))
print(summator())


print("Задача 6")

def slog (sl_1):
    sl_1 = sl_1.title()
    return sl_1

print(slog('zz'))

print("Задача 7")

result_list = []
x = input("Введи что-то: ")
ww = x.split()
for i in ww:
    i=slog(i)
    result_list.append(i)
result_list = ' '.join(result_list)
print(result_list)
