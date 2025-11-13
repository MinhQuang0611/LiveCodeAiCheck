n = int(input())
while n > 0:
    n-=1
    a=(input().split("."))
    ipchuan=True
    if len(a)!=4:
        ipchuan=False
    else:
        for i in a:
            if not i.isdigit() or not (0 <= int(i) <= 255)or (len(i) > 1 and i[0] == '0'):
                ipchuan=False
    if ipchuan==True:
        print("YES")
    else:
        print("NO")