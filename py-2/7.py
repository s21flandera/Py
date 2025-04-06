def cache_deco(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

# Напишите декоратор, который будет кэшировать вызовы функции, которая
# будет передана на вход. То есть декоратор должен проверить нет ли в кэше (
# например, словаре) значения, и если нет, то вычислить и запомнить результат,
# если есть, то взять это значение.
# Входные данные
#
# @cache_deco
# def fib(k):
#     if k <= 2:
#         return 1
#     return fib(k - 1) + fib(k - 2)
# print(fib(30))
# Выходные данные
#
# 832040
