a = list(map(int, input().split()))
ans = [i for i in range(1,len(a)+1) if i not in a]
print(*ans)