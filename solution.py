def fibonacciRecursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

def fibonacciIterative(n):
    a = 0
    b = 1

    for x in range(3,n+1):
        c = a + b
        a = b
        b = c

    return c