def tong(n):
    n = sum(int(digit) for digit in str(n))
    return n
n,p = list(map(int,input().split()))
if tong(n**p) == n:
    print("True")
else:
    print("False")