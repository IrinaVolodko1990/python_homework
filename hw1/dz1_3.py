#Найти значение минимального элемента списка.
import random
n =int(input("Введите размер списка: \n"))
A=[random.randint(0,99) for i in range (n)]
print (A)
minimum=A[0]
for i in range (len(A)):
    if A[i]<minimum:
        minimum=A[i]
print(minimum)

