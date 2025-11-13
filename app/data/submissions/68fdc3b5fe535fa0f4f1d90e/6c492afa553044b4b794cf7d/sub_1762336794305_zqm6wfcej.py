n = int(input())
for i in range(n):
    so = input()
    tich = 1
    tong = 0
    for j in range(0,len(so),2):
        tich *= int(so[j])
    for j in range(1,len(so),2):
        tong += int(so[j])
        
    print(f"{tich} {tong}")