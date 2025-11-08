a = input()
dung = 3
if a[0] != '6':
    dung-=1
for i in a:
    if i != '6' and i != '8':
        dung-=1
if '888' in a:
       dung-=1
if dung == 3:
    print('YES')
else:
    print("NO")