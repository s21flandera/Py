def cache_deco(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


def solution(func_map, func_filter, data):
    filtered = (item for item in data if func_filter(item))
    mapped = (func_map(item) for item in filtered)
    for i, j in enumerate(mapped):
        if i % 2 == 0:
            yield j

code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)

# Необходимо написать генераторную функцию solution, которая будет
# фильтровать данные из последовательности data функцией func_filter, к полученным
# данным применять функцию func_map и возвращать в качестве значения каждый второй
# элемент полученной последовательности. Нужно пользоваться здесь концепцией генератора,
# то есть обрабатывать не все данные разом, а только те, что необходимы для возвращения
# следующего значения.
# Входные данные
#
# def calc():
#     count = 0
#     @cache_deco
#     def calc_(x):
#         nonlocal count
#         count += 1
#         print("Call:", count)
#         return x
#     return calc_
# for i in solution(calc(), lambda x: x % 2 == 1, (1, 1, 2, 2, 2, 3, 1, 2, 3, 1)):
#     print(i)
# Выходные данные
#
# Call: 1
# 1
# Call: 2
# 3
# 3