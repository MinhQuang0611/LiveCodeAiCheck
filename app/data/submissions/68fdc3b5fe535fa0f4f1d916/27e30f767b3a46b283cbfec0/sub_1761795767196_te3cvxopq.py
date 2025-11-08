def nen(s):
    chuoi = ''
    counter = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            counter += 1
        else:
            chuoi += str(counter) +s[i-1]
            counter = 1
    chuoi += str(counter) +s[-1]
    return chuoi
t = int(input())
for _ in range(t):
    s = input()
    ans = nen(s)
    print(ans)


            

