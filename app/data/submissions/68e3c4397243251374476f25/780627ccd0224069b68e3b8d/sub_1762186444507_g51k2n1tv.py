def sangnt(n):
    if n < 2:
        return 0
    sang = [True] * n
    sang[0] = sang[1] = False  
    for i in range(2, int(n**0.5) + 1):
        if sang[i]:
            for j in range(i*i, n, i):
                sang[j] = False
    return sum(sang)


n = int(input())
print(sangnt(n))