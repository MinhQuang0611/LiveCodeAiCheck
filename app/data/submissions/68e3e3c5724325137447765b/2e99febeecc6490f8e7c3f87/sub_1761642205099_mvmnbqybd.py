n = int(input())
s = 0
if n<0:n = -(n)
while n>0:
    a = n%10
    s+= a
    n = n //10
print(s)