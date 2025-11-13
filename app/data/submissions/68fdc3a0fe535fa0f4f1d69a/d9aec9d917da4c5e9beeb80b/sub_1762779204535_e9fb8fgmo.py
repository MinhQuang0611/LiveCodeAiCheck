t = int(input())
for i in range(t):
    n = int(input())
    q = []
    for i in range(n):
        x,y = map(int, input().split())
        q.append((x, y))
    q.sort(key=lambda x: x[1])
ct = 0
end = -1
for x,y in q:
    if x >= end:
        ct += 1
        end = y
print(ct)