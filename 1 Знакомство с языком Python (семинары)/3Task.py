# Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите значение X: "))
y = int(input("Введите значение Y: "))

if x !=0 and y != 0:
    if x>0 and y>0:
        result = "Четверти, в которой находится эта точка - 1"
    elif x<0 and y>0:
        result = "Четверти, в которой находится эта точка - 2"
    elif x<0 and y<0:
        result = "Четверти, в которой находится эта точка - 3"
    elif x>0 and y<0:
        result = "Четверти, в которой находится эта точка - 4"
else:
    result = "Пожалуйста введите значения отличные от 0"
print(result)

