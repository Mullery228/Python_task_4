import random

n = int(input('Введите количество кустов: '))
array = list()
array_2 = list()
for i in range(n):
    m = random.randint(10, 25)
    array.append(m)

array_2 = list()
for i in range(len(array) - 1):
    array_2.append(array[i - 1] + array[i] + array[i + 1])
array_2.append(array[-2] + array[-1] + array[0])
print(max(array_2))
