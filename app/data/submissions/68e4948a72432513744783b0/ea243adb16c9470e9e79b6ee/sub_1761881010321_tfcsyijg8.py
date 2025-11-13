n = int(input())
while n > 0:
    if n % 2 == 0: 
       print(n, end=" ")
       n //= 2
    if n == 1:
        print(n, end=" ")
        break
    if not n % 2 == 0:
        print(n, end=" ")
        n = n*3 + 1
    