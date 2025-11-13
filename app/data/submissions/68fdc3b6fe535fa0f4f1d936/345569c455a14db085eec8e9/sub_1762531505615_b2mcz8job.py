def dinh(c):
    d = len(c)
    if d <3:
        return False
    j = 0
    while j +1<d and c[j]<c[j+1]:
        j+=1
    if j ==0 or j ==d-1:
        return False
    while j +1 < d and c[j]>c[j+1]:
        j+=1
    return j == d-1
a = int(input())
for _ in range(a):
    s = input().strip()
    b = [int(i) for i in s]
    if dinh(b):
        print('YES')
    else:
        print('NO')   
