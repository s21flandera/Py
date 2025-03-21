a = list(map(int, input().split()))
seq = range(a[0], a[1], a[2])
for i in map(lambda x: x ** 2 if x % 2 == 1 else x * -1, seq):
    print(i)
