from typing import List


def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    a = []
    b = []
    for i, j in enumerate(nums1):
        a.append(i)
    for n in range(len(nums1)):
        if nums1[n] < nums2[n]:
            b.append(a[n])
    return b
    # return [i for i, (x, y) in enumerate(zip(nums1, nums2)) if x < y]

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

# Написать функцию get_indexes которая принимает два списка и возвращает
# список индексов, в которых элемент из первого списка меньше элемента из второго
# списка по данному индексу. Желательно проходиться сразу по двум массивам одновременно
# (вспомните функцию zip). Для нахождения индексов можно использовать enumerate вместе с zip.



