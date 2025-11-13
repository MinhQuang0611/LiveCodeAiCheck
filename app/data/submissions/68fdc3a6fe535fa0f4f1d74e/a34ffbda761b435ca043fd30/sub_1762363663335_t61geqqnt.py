n = int(input())
for i in range(n):
    m = list(map(int, input().split()))
    m.sort()
    a = []
    a.append(int(m[0]))
    a.append(int(m[1]))
    a.append(int(m[2]))
    print(sum(a))