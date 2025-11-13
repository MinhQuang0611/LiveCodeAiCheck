t = int(input())

x = []
while t > 0:
    t -= 1
    s = input().strip()
    so = ''
    for ch in s:
        if ch.isdigit():
            so += ch
        else:
            if so != '':
                x.append(int(so))
                so = ''
    if so != '':
        x.append(int(so))
    
x.sort()
for i in x:
    print(i, end="\n") 
