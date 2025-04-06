from typing import List, Dict


def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    s_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    lis = []
    for k, v in s_d.items():
        lis.append(k)
    return lis


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)



# Представьте, что у вас есть словарь с ключами и их частотами
# (то есть насколько часто встречался каждый ключ)  в качестве значений.
# Напишите функцию make_most_common_keys, которая принимает словарь частот и выводит
# отсортированный (например через функцию sorted) по убыванию частот (то есть значений
# ключей) список ключей.

# Входные данные
#
# d =  {5:3, 3:5, 0:2, 4:6, 7:10}
# print(make_most_common_keys(d))
#
# Выходные данные
#
# [7, 4, 3, 5, 0]