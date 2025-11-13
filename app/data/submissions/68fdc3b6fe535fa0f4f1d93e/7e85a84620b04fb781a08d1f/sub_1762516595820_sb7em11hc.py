n = int(input())
m = list(map(int, input().split()))
m = [x for x in m if x != max(m) and x != min(m) ]
c = 0 
for i in m:
     c+=i
     a=c//len(m)
print(a)