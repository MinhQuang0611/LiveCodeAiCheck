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
        if p[i]:
            if(i < 10): 
                print(i, end = " ")
                continue
            rev = dao(i)
            if p[rev]:
                print(i, rev, end = " ")


