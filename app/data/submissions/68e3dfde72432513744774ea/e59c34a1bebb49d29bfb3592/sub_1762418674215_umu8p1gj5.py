n = list(map(int,input().split()))
missing = [i for i in range(1,len(n)) if i not in n]
print(*missing)