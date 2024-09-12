import random

x = random.randint(3, 20)   # случайно выпавшее число в первом поле)
print(x)

n = input('Введите выпавшее число: ')   # скорее введите число для получения пароля)

result = ''
for i in range(1, int(n) + 1):
    for j in range(i + 1, int(n) + 1):
        if int(n) % (i + j) == 0:
            result = result + str(i) + str(j)

print('Пароль: ', result)   # пароль получен, ворота открываются и Вы свободны)))
