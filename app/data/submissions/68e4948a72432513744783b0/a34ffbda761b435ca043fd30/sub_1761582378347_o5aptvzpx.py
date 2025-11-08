n = int(input())
b = [n]
while n != 1:
    if n % 2 == 0:
        n //=2
    else:
        n=n*3+1
    b.append(n)
print(' '.join(map(str, b)))