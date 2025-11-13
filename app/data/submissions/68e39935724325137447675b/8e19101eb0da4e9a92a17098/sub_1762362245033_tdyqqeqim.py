x = int(input())
nn = -2**31
ln = 2**31 - 1
check = -1 if x < 0 else 1
x = abs(x)
r = str(x)[::-1]
rev = int(r) * check
if rev < nn or rev > ln:
    print(0)
else:
    print(rev)
