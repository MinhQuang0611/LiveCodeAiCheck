n = int(input())
while n != 1:
    if n % 2 == 0:
        print(n, end = ' ')
        n //= 2
    elif n % 2 != 0:
        print(n, end = ' ')
        n = n*3 + 1
    elif n == 1:
        print(n)
print(1)

        
