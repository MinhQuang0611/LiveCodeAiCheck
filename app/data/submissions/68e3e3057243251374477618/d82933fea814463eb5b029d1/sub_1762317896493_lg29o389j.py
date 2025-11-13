F = [0,1]
n = int(input())

if n <= 0:
    print()
elif n == 1:
    print(0)
else:
    for i in range(2, n):
        F.append(F[i-1]+F[i-2])

    print(*F[:n])