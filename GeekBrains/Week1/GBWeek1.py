import random

#1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

def task1():
    a = 5
    print("%d = %s" % (a, bin(a)))
    b = 6
    print("%d = %s" % (b, bin(b)))

    print("logical operator AND: %d & %d = %d (%s)" % (a, b, a & b, bin(a & b)))
    print("logical operator OR: %d | %d = %d (%s)" % (a, b, a | b, bin(a | b)))
    print("logical operator EXCLUSIVE OR: %d ^ %d = %d (%s)" % (a, b, a ^ b, bin(a ^ b)))
    print("two bits right shift: %d << 2 = %d (%s)" % (a, a << 2, bin(b << 2)))
    print("two bits left shift: %d >> 2 = %d (%s)" % (a, a >> 2, bin(b >> 2)))


#task1()

#2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

def task2():
    print("point coordinates A(x1;y1):")
    x1 = float(input("\tx1 = "))
    y1 = float(input("\ty1 = "))

    print("point coordinates B(x2;y2):")
    x2 = float(input("\tx2 = "))
    y2 = float(input("\ty2 = "))

    print("Equation of a line passing through these points:")
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(" y = %.2f*x + %.2f" % (k, b))


#task2()

#3. Написать программу, которая генерирует в указанных пользователем границах:
#a. случайное целое число,
#b. случайное вещественное число,
#c. случайный символ.

def task3():
    m1 = int(input("Enter number 1: "))
    m2 = int(input("Enter number 2: "))
    int_num = int(random.random() * (m2 - m1)) + m1
    print(int_num)

    f1 = float(input("Enter float number 1: "))
    f2 = float(input("Enter float number 2: "))
    float_num = float(random.random() * (f2 - f1)) + f1
    print(float_num)

    ch1 = ord(input("Enter symbol 1: "))
    ch2 = ord(input("Enter symbol 2: "))
    n = int(random.random() * (ch2 - ch1)) + ch1
    print(chr(n))


#task3()

#4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

def task4():
    ch1 = ord(input("Enter symbol 1: "))
    ch2 = ord(input("Enter symbol 2: "))
    ch1 = ch1 - ord('a') + 1
    ch2 = ch2 - ord('a') + 1
    print("Positions: %d and %d" % (ch1, ch2))
    print("Letter spacing:", abs(ch1-ch2))


#task4()

#5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

def task5():
    ch1 = int(input("Enter symbol: "))
    ch1 = ch1 + ord('a') - 1
    print('This is: ', chr(ch1))


#task5()

#6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков.
#Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

def task6():
    a = float(input("Side a: "))
    b = float(input("Side b: "))
    c = float(input("Side c: "))

    if a + b <= c or b + c <= a or a + c <= b:
        print("this triangle is not exist!")
    elif a == b == c:
        print("equilateral triangle")
    elif a != b and b != c and c != a:
        print("miscellaneous triangle")
    elif c ** 2 == a ** 2 + b ** 2:
        print("right triangle")
    else:
        print("isosceles triangle")


#task6()

#7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

def task7():
    year = int(input("Enter year: "))
    if year % 4 == 0:
        print("leap year")
    else:
        print("don't leap year")


#task7()

#8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def task8():
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    num3 = float(input("Number 3: "))

    if num1 < num2 < num3 or num1 > num2 > num3:
        print("Average: ", num2)
    elif num2 < num3 < num1 or num2 > num3 > num1:
        print("Average: ", num3)
    elif num3 < num1 < num2 or num3 > num1 > num2:
        print("Average: ", num1)
    else:
        print("Numbers must not be equal")


#task8()