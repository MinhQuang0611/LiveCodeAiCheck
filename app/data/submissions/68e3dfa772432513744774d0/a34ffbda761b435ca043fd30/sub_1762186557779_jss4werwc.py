a = list(map(int, input().split()))
if len(a)<3:
    print(max(a))
else:
    a.remove(max(a))
    a.remove(max(a))
    print(max(a))