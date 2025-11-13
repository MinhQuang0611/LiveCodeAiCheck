n = input()
ds = list(n)

sl = len(ds)
for i in range(0,sl,3):
    a = sl - i
    if (a != sl):
        ds.insert(a,",")
kq =''.join(ds)
print(kq)
