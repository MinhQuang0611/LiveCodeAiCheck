n = int(input())
if n < 0:
    n = abs(n)
total = sum(int(so) for so in str(n))
print(total)