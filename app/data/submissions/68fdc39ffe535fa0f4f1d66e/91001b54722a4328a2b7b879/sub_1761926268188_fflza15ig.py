n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
group = 1 
for i in range(1, n):
    if a[i] - a[i -1] > k:
        group += 1
print(group)