a =int(input())
for _ in range(a):
    s = input().strip()
    b = ""
    dem = 1
    for i in range(1,len(s)):
        if s[i] ==s[i-1]:
            dem +=1
        else:
            b += str(dem) +s[i-1]
            dem = 1
    b += str(dem) +s[-1]
    print(b)