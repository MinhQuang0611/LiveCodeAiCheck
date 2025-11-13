def nt(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def dn(n):
    s = str(n)
    tmp = s[::-1]
    return  int(tmp)

n = int(input())
a = list(map(int, input().split()))

for i in a:
    if nt(i) == True and nt(dn(i)) == True:
        print("YES")
    else:
        print("NO")
