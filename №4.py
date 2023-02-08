# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


number = int(input('Введите число: '))
mi_listr = " "
while number != 0:
    mi_listr = str(number % 2) + mi_listr
    number //= 2
print(mi_listr)