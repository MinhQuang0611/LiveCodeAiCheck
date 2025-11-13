n = int(input())
arr = list(map(int,input().split()))
total = (sum(arr) - max(arr) - min(arr)) / (len(arr) - 2)
print(total)
