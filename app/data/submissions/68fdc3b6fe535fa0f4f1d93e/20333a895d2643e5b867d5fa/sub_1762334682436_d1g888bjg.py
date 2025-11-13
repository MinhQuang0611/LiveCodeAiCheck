n = int(input())
m = list(map(float,input().split()))
min_m=min(m)
max_m=max(m)
m = [x for x in m if x != min_m and x !=max_m]
a = 0
for i in m:
    a = a + i
h = a/len(m)
k = round(h,2)
print(int(k))