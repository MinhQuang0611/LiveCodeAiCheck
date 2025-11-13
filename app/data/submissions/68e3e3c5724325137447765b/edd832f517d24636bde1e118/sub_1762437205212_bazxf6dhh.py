n = int(input())
m = abs(n)
a = 0
while m != 0:
    a += m % 10
    m //= 10
print(a)