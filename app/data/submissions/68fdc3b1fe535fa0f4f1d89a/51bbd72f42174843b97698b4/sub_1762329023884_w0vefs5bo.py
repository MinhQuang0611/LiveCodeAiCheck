n = input()
count = 0
tong = 0
for i in n:
    tong += int(i)
    
while tong > 9:
    tong = sum(int(i) for i in str(tong))
    count += 1
        
print(count)
    