print(x[::-1], end = ' ')


l_func = lambda x: 2 ** x
def l_func(x):
    return 2 ** x


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n -1)
def factorial(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result
