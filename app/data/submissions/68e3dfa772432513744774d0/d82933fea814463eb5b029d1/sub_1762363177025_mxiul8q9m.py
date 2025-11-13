n = list(map(int, input().split()))
a = n
a.remove(max(a))
a.remove(max(a))
print(max(a))