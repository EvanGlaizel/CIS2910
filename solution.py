def fibbonaciRecursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    return fibbonaciRecursive(n-1) + fibbonaciRecursive(n-2)

def fibbonaciIterative(n):
    a = 0
    b = 1

    for x in range(3,n+1):
        c = a + b
        a = b
        b = c

    return c


print(fibbonaciIterative(8))