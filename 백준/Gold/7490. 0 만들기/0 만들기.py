import sys

input = sys.stdin.readline


def iszero(input_string):
    num = int(input_string[0])
    sum_all = 0
    input_string = input_string[1:]
    isNegative = False
    isOperation = False

    for word in input_string:
        if word == "+":
            isNegative = False
            isOperation = True
        elif word == "-":
            isNegative = True
            isOperation = True
        elif word == " ":
            num *= 10
        else:
            if isNegative:
                num -= int(word)
            else:
                num += int(word)

        if isOperation:
            sum_all += num
            num = 0
            isOperation = False
    sum_all += num

    if sum_all == 0:
        for i in expression:
            print(i, end="")
        print()
    return


def printSumZeroExpression(expression, oper_cnt=0):
    if oper_cnt == (len(expression) // 2):
        iszero(expression)
        return

    oper_cnt += 1
    for operator in (" ", "+", "-"):
        expression[oper_cnt * 2 - 1] = operator
        printSumZeroExpression(expression, oper_cnt)
    oper_cnt -= 1


for _ in range(int(input())):
    n = int(input())
    expression = [1]
    for i in range(2, n + 1):
        expression.append(" ")
        expression.append(i)
    printSumZeroExpression(expression)
    print()
