def fib(n):
    a, b = 1, 1
    for i in range(n-1):
            a, b = b, a + b
    return a

#series
for i in range(10):
    fib(i+1)
