from collections import deque

# Nhập dữ liệu
n, m = map(int, input().split())

# Tạo danh sách kề (adjacency list)
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

# Đọc m cặp (a, b)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# Queue lưu các node có indegree = 0
q = deque([i for i in range(1, n + 1) if indegree[i] == 0])
order = []  # kết quả topo

while q:
    u = q.popleft()
    order.append(u)
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

# Nếu sắp xếp được đủ n khóa học
if len(order) == n:
    print(*order)
else:
    print("IMPOSSIBLE")
