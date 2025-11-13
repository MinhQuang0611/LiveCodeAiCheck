t=int(input())
for i in range(t):
    a=input()
    b=list(a)
    if b[0]==b[-1]:
        print('YES')
    else:
        print('NO')