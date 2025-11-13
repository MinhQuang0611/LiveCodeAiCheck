t = int(input())
for _ in range(t):
    s = input()
    tong = sum(int(i) for i in s)
    k = (tong % 10 == 0)
    b = True
    for i in range(len(s)-1):
        if abs(int(s[i])) - int(s[i + 1]) != 2:
            b = False
            break
    if k and b:
        print("YES")
    else:
        print("NO")     
