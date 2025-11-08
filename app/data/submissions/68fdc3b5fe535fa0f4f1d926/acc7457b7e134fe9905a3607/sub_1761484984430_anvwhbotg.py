for _ in range(int(input())):
    n = int(input()) 
    a = [0] * n
    used = set()

    total = 0
    def Count(i):
        global total
        for j in range(n, 0, -1):
            if j not in used:
                used.add(j)
                a[i] = j
                if i < n - 1:
                    Count(i + 1)
                else:
                    total += 1
                used.remove(j)

    Count(0)
    print(total)
    used.clear()  

    def Try(i):
        for j in range(n, 0, -1):
            if j not in used:
                used.add(j)
                a[i] = j
                if i < n - 1:
                    Try(i + 1)
                else:
                    print(''.join(map(str, a)), end=" ")
                used.remove(j)

    Try(0)
    print()
