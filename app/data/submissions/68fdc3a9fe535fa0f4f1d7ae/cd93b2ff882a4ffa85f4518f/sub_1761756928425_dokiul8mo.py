n = int(input())
a = []
for i in range(0,n):
    s = input()
    num = ''
    for c in s:
        if c.isdigit():
            num += c
        else:
            if num:
                a.append(int(num))
                num = ''
    if num:
        a.append(int(num))
a.sort()
for i in range (0,len(a)):
    print(a[i])