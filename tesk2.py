# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

N = int(input('Введите число: '))
list1 = []
for i in range(2, N+1):
    if N % i == 0:
        count = 1
        for j in range(2, (i//2+1)):
            if i % j == 0:
                count = 0
        if (count ==1):
            list1.append(i)
print(list1)
