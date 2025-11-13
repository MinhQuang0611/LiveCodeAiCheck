t = int(input())
a, b, c = map(int,input().split())
d = 0
while a <= c:
    a += t*(a*(b/100))
    d += 1
print(d)