# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

array = [0] * 8

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            array[j-2] += 1

i = 0
while i < len(array):
    print(f'{i + 2} - {array[i]}')
    i += 1