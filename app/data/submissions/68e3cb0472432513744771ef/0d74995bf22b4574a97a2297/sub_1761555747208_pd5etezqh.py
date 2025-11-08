def digitalroot(n):
    while n >= 10:
        n = sum(int(so) for so in str(n))
    return n
n = int(input())
print(digitalroot(n))