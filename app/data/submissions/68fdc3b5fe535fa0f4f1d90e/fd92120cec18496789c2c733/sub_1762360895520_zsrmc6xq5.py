t = int(input()) #số lượng

for i in range (t):
    tong = 0
    tich = 1
    n = input() #số dạng str
    for j in range (len(n)):
        if (j+1) % 2 == 0:
            tong += int(n[j])
        else:
            tich *= int(n[j])
    print (tich, tong)
    
                
            
            
    