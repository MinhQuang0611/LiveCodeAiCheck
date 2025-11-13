a=[int(x) for x in input().split()]
a=sorted(a)
print(a[-3] if a[-3]<a[-2] and a[-3]<a[-1] else a[-1])