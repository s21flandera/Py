a = list(map(int, input().split()))
seq = range(a[0], a[1], a[2])
for i in map(lambda x: x ** 2 if x % 2 == 1 else x * -1, seq):
    print(i)
# напишите код, который также будет использовать функцию map() и лямбда функцию.
# На вход будут подаваться три аргумента для range: начало, конец и шаг числовой
# последовательности. Нужно вывести для каждого элемента range квадрат числа, если
# число нечетное, иначе вывести противоположное ему. (Решение можно реализовать в две
# и даже в одну строку!)
# Входные данные
#
# 1 10 1
# Выходные данные
#
# 1
# -2
# 9
# -4
# 25
# -6
# 49
# -8
# 81