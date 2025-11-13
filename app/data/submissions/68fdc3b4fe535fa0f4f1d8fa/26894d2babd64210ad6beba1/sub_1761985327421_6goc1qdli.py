def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n% i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))

while(True):
    check = True
    for i in range(n - 1):
        if(not snt(a[i])):
            continue
        else:
            for j in range(i, n):
                if not snt(a[j]):
                    continue
                else:
                    if(a[i]>a[j]):
                        check = False
                        t = a[j]
                        a[j] = a[i]
                        a[i] = t
    if check == True:
        break
print(*a, end = " ")
