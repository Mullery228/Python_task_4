import random

n = int(input('Введите размер первого списка: '))
m = int(input('Введите размер второго списка: '))
array_1 = [0] * n
array_2 = [0] * m
new_array = [0]

for i in range(n):
    array_1[i] = random.randint(0, 10)

for i in range(n):
    array_2[i] = random.randint(0, 10)

for i in range(n):
    for j in range(m):
        if array_1[i] == array_2[j]:
            for k in range(len(new_array)):
                if array_2[j] != new_array[k]:
                    new_array.append(array_2[j])


new_array_2 = list(set(new_array))
new_array_2.pop(0)
print(sorted(new_array_2))
