t=int(input())
for i in range (t):
    s=input()
    tong=0
    flag=True
    for j in range (len(s)-1):
        tong+=int(s[j])
        int(s[j])-int(s[j+1])
        if abs(int(s[j])-int(s[j+1]))!=2:
            flag=False
            break
    tong+=int(s[j+1])
    if tong %10 == 0 and flag:
        print('YES')
    else:
        print("NO")