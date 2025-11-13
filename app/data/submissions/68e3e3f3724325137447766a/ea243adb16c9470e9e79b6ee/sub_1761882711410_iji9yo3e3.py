n = int(input())
new_n = 0
while n > 0:
    sodu = n % 10
    new_n = new_n*10 + sodu
    n //= 10
print(new_n)