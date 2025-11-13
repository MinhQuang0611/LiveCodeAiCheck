t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().split()) 
    A = []
    for i in range(n):
        row = list(map(int, input().split()))
        A.append(row)
    for i in range(n):
        hang = []
        for j in range(n):
            s = 0
            for k in range(m):
                s += A[i][k] * A[j][k]
            hang.append(str(s))
        print(" ".join(hang))