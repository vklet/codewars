
def fibonacci(n):
    if n < 1:
        yield 0
    elif n < 3:
        yield 1
    a, b = 1, 0
    for _ in range(2, n, 1):
        a, b = a + b, a
        yield a + b

#*_, last = fibonacci(0)

print(list(fibonacci(-1)))
#print(last)
