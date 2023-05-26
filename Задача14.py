# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("erg: "))

flask = True
i = 2
print(1)
if n == 1:
    flask = False

while flask:
    print(f"{i} ")
    i *= 2
    if i >= n:
        flask = False
