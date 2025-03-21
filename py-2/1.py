def av(a):
    c = 0
    a = a.split()
    d = list(map(int, a))
    for i in range(len(a)):
        c += d[i]
    print(round(c/len(a), 2))


while b := input():
    av(b)
