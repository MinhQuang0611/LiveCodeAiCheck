def sangnt(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False  

    k = int(n ** 0.5)
    for i in range(2, k + 1):
        if c[i]:  
            for j in range(i * i, n + 1, i):
                c[j] = False  

    arr = [i for i in range(2, n + 1) if c[i]]
    return arr

def snt(n):
    if (n == 2) or (n == 3):
        return True
    if (n < 2) or (n % 2 == 0) or (n % 3 == 0):
        return False
    kt = int(n ** 0.5)
    k = -1
    while True:
        k += 6
        if (n % k == 0) or (n % (k + 2) == 0):
            break
        if k > kt:
            break
    return k > kt

m = int(input())
for i in range(m):
    n = int(input())
    arr = sangnt(n)

    for i in arr:
        st = str(i)
        if i > 9:
            st = st[::-1]
            if snt(int(st)): 
                print(f"{i} {st}", end=' ')
        else:
            print(f"{i}", end = ' ')