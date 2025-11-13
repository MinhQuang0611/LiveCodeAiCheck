t = int(input())
while(t > 0):
    t -= 1
    s = input()
    flag = True
    for i in range(len(s)):
        if(s[i] != s[i-2]):
            flag = False
            break
    if(flag == True): print("YES")
    else: print("NO")