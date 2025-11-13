n = int(input())
m = list(map(float,input().split()))
min_m=min(m)
max_m=max(m)
m.remove(min_m)
m.remove(max_m)
a = 0
for i in m:
    a = a + i
h = a/len(m)
print(round(h,2))

