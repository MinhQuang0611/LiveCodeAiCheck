t = int(input())          
for _ in range(t):
    s = input()           
    kq = ''               
    dem = 1              
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            dem += 1
        else:
            kq += str(dem) + s[i - 1]
            dem = 1
    kq += str(dem) + s[-1] 
    print(kq)