def fibo(n):
    if n == 0:
        return 0
    fib1 = 0
    fib2 = 1
    for x in range(1, n):
        temp = fib1 + fib2
        fib1 = fib2
        fib2 = temp
    return fib2


print(fibo(5))
