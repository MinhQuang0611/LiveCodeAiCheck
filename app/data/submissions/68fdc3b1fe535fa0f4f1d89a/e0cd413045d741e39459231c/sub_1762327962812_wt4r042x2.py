n = input().strip()
dem = 0
while len(n) > 1:
    tong = sum(int(i) for i in n)
    n = str(tong)
    dem += 1

print(dem)
