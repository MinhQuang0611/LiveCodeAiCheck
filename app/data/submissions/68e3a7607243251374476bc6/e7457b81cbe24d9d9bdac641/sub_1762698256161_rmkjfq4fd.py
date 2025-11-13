n = int(input())
count = 0
k = 1

while k <= n:
    high = n // (k * 10)
    cur = (n // k) % 10
    low = n % k

    if cur == 0:
        count += high * k
    elif cur == 1:
        count += high * k + (low + 1)
    else:
        count += (high + 1) * k

    k *= 10

print(count)
