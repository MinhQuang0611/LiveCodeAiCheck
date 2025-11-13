N = 10**6
p = [True] * (N + 3)

def sieve():
    
    p[0] = p[1] = False
    for i in range(2, int(N ** 0.5) + 1):
        if p[i]:
            for j in range(i * i, N + 1, i):
                p[j] = False

def dao(x):
    return int(str(x)[::-1])

t = int(input())
sieve()
for _ in range(t):
    n = int(input())
    res = []
    for i in range(2, n):
        if(i == 2):
            res.append(f"{i} {3}")
            continue
        if(i == 3):
            res.append(f"{i} {2}")
            continue
        if(i == 5):
            res.append(f"{i} {7}")
            continue
        if(i == 7):
            res.append(f"{i} {5}")
            continue
        if p[i]:
            rev = dao(i)
            if p[rev]:
                res.append(f"{i} {rev}")
    print(' '.join(res))
