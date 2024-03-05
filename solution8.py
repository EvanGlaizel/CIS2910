from math import factorial

# takes in n >= 1
# returns the number of possible derangements of n items
# Examples:
# |  Input  |  Output  |
# |---------|----------|
# |    1    |     0    |
# |---------|----------|
# |    2    |     1    |
# |---------|----------|
# |    3    |     2    |
# |---------|----------|
# |    4    |     9    |
# |---------|----------|
# |    5    |    44    |
# |---------|----------|

def fact(n):
    num = 1

    for i in range(1,n + 1):
        num *= i

    return num

def pow(n, p):
    sum = 1

    for i in range(p):
        sum *= n

    return sum

def numDerangements( n ):
    sum = 0

    for i in range(1,n+1):
        sum += (fact(n) // fact(i)) * pow(-1, i - 1)

    return fact(n) - sum

# Testing code provided in main():
def main():
    testArgs = [[1,0],[2,1],[3,2],[4,9],[5,44]]
    for arg in testArgs:
        nArg, answer = arg
        result = numDerangements(nArg)
        if result != answer:
            print(f"Failed numDerangements test with arg n={nArg}.\nExpected: {answer}, Got: {result}")
        else:
            print(f"Passed numDerangements test with arg n={nArg}.")
    return 0

if __name__ == '__main__':
    main()
