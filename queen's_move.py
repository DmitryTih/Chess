#Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
#Программа должна вывести "Yes" , если из первой клетки ходом ферзя можно попасть во вторую или "No" в противном случае.
x1, y1 = int(input("x1: ")), int(input("y1: "))
x2, y2 = int(input("x2: ")), int(input("y2: "))
if abs(x1- x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print("Yes")
else:
    print("No")