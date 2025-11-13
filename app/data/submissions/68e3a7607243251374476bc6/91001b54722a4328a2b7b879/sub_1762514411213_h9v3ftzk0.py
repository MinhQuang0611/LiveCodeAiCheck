n = int(input())
count = 0
i = 1 
while i <= n:
    left = n // (i * 10)
    digit = (n // i) % 10
    right = n % i
    if digit == 0:
        count += left * i
    elif digit == 1:
        count += left * i + right + 1
    else:
        count += (left + 1) * i
    i *= 10
print(count)
