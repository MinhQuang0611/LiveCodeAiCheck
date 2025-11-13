t = int(input())
while(t > 0):
    t -= 1
    s = list(input().strip())
    n = len(s)
    d = 4  

    for i in range(n - 1, 0, -1):  
        if int(s[i]) > d:
            s[i - 1] = str(int(s[i - 1]) + 1)
            for j in range(i, n):
                s[j] = '0'
        if(d == 4): d = 3
        else: d = 4

    if int(s[0]) > 9:
        s = ['1'] + ['0'] * n

    print(''.join(s))
