t = int(input())
for i in range (t):
    s = (input())
    chan=1
    le=0
    for i in range(len(s)):
        if i % 2 == 0:
            chan=chan*int(s[i])
        else:
            le=le+int(s[i])
    print(chan, le)