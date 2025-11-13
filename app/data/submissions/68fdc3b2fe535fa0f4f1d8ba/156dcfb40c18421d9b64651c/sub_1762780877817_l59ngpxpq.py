def dieu_kien(n):
    chu_so = list(map(int, n))         
    tong = sum(chu_so)                  
    hieu_2 = True                      
    for i in range(1, len(chu_so)):
        hieu = abs(chu_so[i] - chu_so[i - 1])  
        if hieu != 2:
            hieu_2 = False               
            break
    return tong % 10 == 0 and hieu_2   
def mat_ma(s):
    for num in s:
        if dieu_kien(num):
            print("YES")
        else:
            print("NO")
t = int(input())          
s = []
for _ in range(t):
    s.append(input().strip())
mat_ma(s)
