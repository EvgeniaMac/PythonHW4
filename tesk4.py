# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

list1 = [1,5,7,3,8,1,5,7,3,8]
print(list1)
list2= list(set(list1))
print(list2)