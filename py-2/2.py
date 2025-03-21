def s(a):
    if a[0] == '!':
        a = a.upper()
    else:
        a = a.lower()
    a = a.translate(str.maketrans('', '', '!@#%'))
    print(a)


while b := input():
    s(b)
