from math import sqrt

def fibonacci(n):
    alpha = ((1+sqrt(5))/2)
    beta = ((1-sqrt(5))/2)
    return int((alpha**n - beta**n)/sqrt(5))


#*_, last = fibonacci(0)

print(fibonacci(2000000))
#print(last)
