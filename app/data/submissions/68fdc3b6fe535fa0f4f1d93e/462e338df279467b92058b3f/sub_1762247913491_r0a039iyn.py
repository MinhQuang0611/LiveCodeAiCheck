n = int(input())
a = list(map(int, input().split()))
a.sort()
if a[0] == a[-1]:
    print(sum(a) / len(a))
else:
    a.pop(0)
    a.pop(-1)
    print(sum(a) / len(a))
