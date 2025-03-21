a = input()
c=['!', '%', '#', '@']
aa=len(a)
for char in c:
    a=a.replace(char, '')
b = aa - len(a) 
print(b)
print(a.lower())