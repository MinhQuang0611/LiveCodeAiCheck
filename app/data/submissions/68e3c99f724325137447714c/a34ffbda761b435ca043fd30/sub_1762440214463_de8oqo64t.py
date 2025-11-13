a = int(input())
b = []
for i in range(1, a):
    if a%i==0:
        b.append(i)
if sum(b)!=a or a == 0:
    print('false')
else:
    print('true')