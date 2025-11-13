n = input()
count = 0
tong = 0
for i in n:
    tong += int(i)
    
while len(str(tong)) >= 1:
    tong_moi = sum(map(int, str(tong)))
    tong = str(tong_moi)
    count += 1
        
print(count)
    