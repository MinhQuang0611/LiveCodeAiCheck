def tachso(n):
    dem = 0
    while n > 0:
        dem += n % 10
        n //= 10
    return dem
def dem(n):
    tmp = 0
    while n > 0:
        tmp += 1
        n //= 10
    return tmp

n = int(input())
b = tachso(n)
tmp = 1
while dem(b) > 1:
    tmp += 1
    b = tachso(b)
    dem(b)
    
print(tmp)