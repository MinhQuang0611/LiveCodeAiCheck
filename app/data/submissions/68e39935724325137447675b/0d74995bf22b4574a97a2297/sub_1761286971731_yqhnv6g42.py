n = input()
dau = ""
so = n
if n.startswith('-'):
    dau = "-"
    so = n[1:]
res1 = so[::-1]
res2 = res1.lstrip('0')
if not res2:
    print("0")
else:
    print(dau + res2)