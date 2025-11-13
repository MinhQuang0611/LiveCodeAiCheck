def nen_so(k):
    ans = 0
    while(k > 0):
        ans += k % 10
        k = k // 10
    return ans

n = int(input())
cnt = 0
while(n > 10):
    n = nen_so(n)
    cnt += 1
print(cnt)