t = int(input())

while t > 0:
    t -= 1
    s = input().strip()
    so = ''
    x = []
    for ch in s:
        if ch.isdigit():
            so += ch
        else:
            if so != '':
                x.append(int(so))
                so = ''
    if so != '':
        x.append(int(so))
    print(min(x))

