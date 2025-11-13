t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(3)]
    total_energy = 0 
    if n >= 3 and m >= 3:
        for i in range(n -2):
            for j in range(m - 2):
                energy = 0
                for x in range(3):
                    for y in range(3):
                        energy += a[i + x][j + y] * b[x][y]
                total_energy += energy
    else:
        for i in range(min(3, n)):
            for j in range(min(3, n)):
                total_energy += a[i][j] * b[i][j]
    print(total_energy)