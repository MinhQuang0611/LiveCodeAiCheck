def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check1(n):
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            q = n // p
            if p!=q and snt(p) and snt(q):
                return True
    return False

def check2(k, n):
    if snt(k) and k**8 <= n:
        return True
    return False

n = int(input())
count = 0
for i in range(2, int(n**0.5) + 1):
    if check1(i) or check2(i, n):
        count += 1
print(count)
