n=int(input())
for i in range (0,n):
    s=input()
    dem=1
    s=s+'@'
    for i in range (0,len(s)-1):
        if s[i]==s[i+1]:
            dem=dem+1
        else:
            print(dem,s[i],sep="",end="")
            dem=1