import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

state = [0] * (n + 1)  # 0 = chưa thăm, 1 = đang thăm, 2 = đã thăm xong
parent = [-1] * (n + 1)
cycle = []

def dfs(u):
    state[u] = 1  # đang thăm
    for v in graph[u]:
        if state[v] == 0:
            parent[v] = u
            if dfs(v):
                return True
        elif state[v] == 1:
            # phát hiện chu trình
            cycle.append(v)
            x = u
            while x != v:
                cycle.append(x)
                x = parent[x]
            cycle.append(v)
            cycle.reverse()
            return True
    state[u] = 2  # thăm xong
    return False

found = False
for i in range(1, n + 1):
    if state[i] == 0:
        if dfs(i):
            found = True
            break

if not found:
    print("IMPOSSIBLE")
else:
    print(len(cycle))
    print(*cycle)
