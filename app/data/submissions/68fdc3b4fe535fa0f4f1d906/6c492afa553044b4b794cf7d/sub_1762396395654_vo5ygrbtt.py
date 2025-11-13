n = int(input())
for i in range(n):
    st = input()
    if st[0] == st[len(st)-1]:
        print('YES')
    else:
        print('NO')