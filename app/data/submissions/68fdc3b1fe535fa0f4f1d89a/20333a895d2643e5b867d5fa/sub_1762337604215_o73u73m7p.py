s = input().strip("-0")
m=map(int,s)
a = 0

while len(s) > 1:
    s = str(sum(m))
    a = a + 1

print(a)