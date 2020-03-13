# Task_A
"""
sumIn = open('project1/TaskA/sumIn.txt', 'r')
numbers = sumIn.read()
print(numbers)
sumIn.close() #Закрываем дескриптор файла(?)

num1 = int(numbers[0])
num2 = int(numbers[2])
sum = num1 + num2
print(sum)

sumOut = open('project1/TaskA/sumOut.txt', 'w')
sumOut.write("{:d}".format(sum))
sumOut.close()
"""

# TaskB
"""
numbersIn = open('project1/TaskB/numbersIn.txt', 'r')
numbers = numbersIn.read()
print(numbers)
numbersIn.close()

A = int(numbers[0])
B = int(numbers[2])


def condition(con1):
    if con1 <= 1:
        print('Ошибка.Число меньше, либо равно 1')
    elif con1 >= 100:
        print('Ошибка.Число больше, либо равно 100')
    else:
        print("Вы ввели:{:d}".format(con1))

condition(A)
condition(B)
rangeLeft = -10000
rangeRight = 10000
for X in range(rangeLeft, rangeRight):
    Y = int((1 - A*X)/B)
    if A*X+B*Y == 1:
        X_Success = X
        Y_Success = Y
        print(X_Success, Y_Success)
    else:
        print("Условие не выполняется!")

numbersOut = open('project1/TaskB/numbersOut.txt', 'w')
numbersOut.write("{:d} {:d}".format(X_Success, Y_Success))
numbersOut.close()
"""

#TaskC
"""greatestIn = open('project1/TaskC/greatestIn.txt', 'r')
alphabet = greatestIn.read()
print(alphabet)
greatestIn.close()

MaxChar = max(alphabet)

greatestOut = open('project1/TaskC/greatestOut.txt', 'w')
greatestOut.write(str.format(MaxChar))
greatestOut.close()"""

#TaskD
"""primeIn = open('project1/TaskD/primeIn.txt', 'r')
number = int(primeIn.read())
print(number)

while number > 1:
    i = 2
    numberList = []
    while number != 1:
        if number % i == 0:
            number = number // i
            print(i, end=' ')
            print("\nNumber = ", number)
            numberList.append(i)
        else:
            i += 1
            print("i = ", i)
    print("list = ", numberList)

primeOut = open('project1/TaskD/primeOut.txt', 'w')
for element in numberList:
    primeOut.write("%s " % element)
primeOut.close()
"""