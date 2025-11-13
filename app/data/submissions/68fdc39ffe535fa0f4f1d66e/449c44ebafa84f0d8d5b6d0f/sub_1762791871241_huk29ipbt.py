n, k = map(int, input().split())
n = list(map(int, input().split()))
n.sort()
cnt = 1
for i in range(1, len(n)):
    if n[i] - n[i-1] > k:
        cnt += 1
print(cnt)



