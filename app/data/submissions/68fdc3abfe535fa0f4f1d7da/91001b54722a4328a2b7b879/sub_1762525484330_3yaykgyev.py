q = int(input())
parent = [i for i in range(10001)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra
for _ in range(q):
    u, v, t = map(int, input().split())
    if t == 1:
        union(u, v)
    else:
        print(1 if find(u) == find(v) else 0)
