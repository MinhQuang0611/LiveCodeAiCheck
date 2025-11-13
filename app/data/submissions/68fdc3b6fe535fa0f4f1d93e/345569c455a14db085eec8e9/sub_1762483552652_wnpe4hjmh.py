from functools import reduce
a = int(input())
b = list(map(int,input().split()))
c = [x for x in b if x!= max(b) and x != min(b)]
d = reduce(lambda y,z: y+z , c)
print(d//len(c))