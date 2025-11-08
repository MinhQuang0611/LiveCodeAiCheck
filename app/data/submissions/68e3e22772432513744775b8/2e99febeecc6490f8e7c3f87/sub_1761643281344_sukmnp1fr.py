def gt(n):
    if n==0 or n==1:
        return 1
    else:
        return n*gt(n-1)
n = int(input())
print(gt(n))
