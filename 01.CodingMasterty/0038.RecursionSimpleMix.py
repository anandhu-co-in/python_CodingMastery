# Find power of a number using recursion
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


# Find factorial of a number using recursion
def factorial(x):
    if x <= 0:
        return 0
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)


# Product of an array using recursion
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * productOfArray(arr[1:])


# Recursive range
def recursiveRange(n):
    if n == 0:
        return 0
    else:
        return n + recursiveRange(n - 1)


# Fibonacci
def fibonacci(n):
    if n <= 2: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(power(2, 4))
print(factorial(4))
print(productOfArray([10, 20, 2, 4]))
print(recursiveRange(5))
print(fibonacci(6))
