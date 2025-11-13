a = input().strip()
dem = 0
while len(a)>1:
    total = sum(int(x) for x in a)
    a = str(total)
    dem += 1
print(dem)