a = int(input())
b = float(input())
c = int(input())
print(f'{a:0=+10}')
print(f'{b:#>10.2f}')
cc = f'{c:b}'
if len(cc) > 16:
    cc = cc[:16]
while len(cc) < 16 or len(cc) % 4 !=0:
    cc = '0' + cc

result = '_'.join([cc[i:i+4] for i in range(0, len(cc), 4)])
print(result)