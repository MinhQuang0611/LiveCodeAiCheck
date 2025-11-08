from collections import deque

# Đọc toàn bộ dãy số trong một dòng
data = list(map(int, input().split()))

n, m = data[0], data[1]
pairs = data[2:]  # phần còn lại là các cặp (a, b)

# Tạo đồ thị
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

# Duyệt từng cặp (a, b)
for i in range(0, len(pairs), 2):
    a, b = pairs[i], pairs[i + 1]
    graph[a].append(b)
    indegree[b] += 1

# Hàng đợi các khóa có indegree = 0
q = deque([i for i in range(1, n + 1) if indegree[i] == 0])
order = []

while q:
    u = q.popleft()
    order.append(u)
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

# Kết quả
if len(order) == n:
    print(*order)
else:
    print("IMPOSSIBLE")
