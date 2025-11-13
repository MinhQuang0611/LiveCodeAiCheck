t = int(input())
for _ in range(t):
    matrix_mn = []
    matrix_33 = []
    total_sum = 0
    n, m = map(int, input().split())
    for _ in range(n):
        current = list(map(int, input().split()))
        matrix_mn.append(current)
    for _ in range(3):
        current = list(map(int, input().split()))
        matrix_33.append(current)
    
    for i in range(n - 2):#cot
        for j in range(m - 2):#hang
            s = 0
            for ki in range(3):
                for kj in range(3):
                    s += matrix_mn[i+ki][j+kj] * matrix_33[ki][kj]
            total_sum += s
    print(total_sum)