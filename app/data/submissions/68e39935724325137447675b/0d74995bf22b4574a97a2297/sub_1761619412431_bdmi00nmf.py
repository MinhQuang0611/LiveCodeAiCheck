n = input()
dau = ""
so = n
if n.startswith('-'):
    dau = "-"
    so = n[1:]
res1 = so[::-1]
res2 = res1.lstrip('0')
if res2 == "":
    result = 0
else:
    result = int(dau + res2)
if result < -2**31 or result > 2**31 - 1:
    print(0)
else:
    print(result)
