def taskA():
    pathIn = 'project1/TaskA/sumIn.txt'
    pathOut = 'project1/TaskA/sumOut.txt'
    first = 0
    second = 1
    with open(pathIn, 'r') as file:
        numbers = file.read()
        print(numbers)

    numList = numbers.split(" ")
    print(numList)

    num1 = int(numList[first])
    num2 = int(numList[second])
    sum = num1 + num2
    print(sum)

    with open(pathOut, 'w') as file:
        file.write("%d" % sum)

#taskA()

def TaskB():
    pathIn = 'project1/TaskB/numbersIn.txt'
    pathOut = 'project1/TaskB/numbersOut.txt'
    rangeLeft = -10000
    rangeRight = 10000
    firstNum = 0
    secondNum = 1

    with open(pathIn, 'r') as file:
        numbers = file.read()
        print(numbers)

    numList = numbers.split(" ")
    print(numList)
    A = int(numList[firstNum])
    print(A)
    B = int(numList[secondNum])
    print(B)

    def condition(con1):
        for con1 in range(2, 100):
            if con1 <= 1:
                print('Ошибка.Число меньше, либо равно 1')
                print("break1")
                break
            elif con1 >= 100:
                print('Ошибка.Число больше, либо равно 100')
                print("break2")
                break
        else:
            print("Вы ввели:%d" % con1)

    condition(-2)
    condition(B)

    X_Success = X
    Y_Success = Y

    for X in range(rangeLeft, rangeRight):
        Y = int((1 - A*X)/B)
        if A*X+B*Y == 1:
            print(X_Success, Y_Success)
            print("break")
            break
        else:
            print("Условие не выполняется!")
    else:
        print("no break")
    with open(pathOut, 'w') as file:
        file.write("%d %d" % X_Success % Y_Success)

TaskB()
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
            number /= i
            print(i, end=' ')
            print("\nNumber = %d" % number)
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