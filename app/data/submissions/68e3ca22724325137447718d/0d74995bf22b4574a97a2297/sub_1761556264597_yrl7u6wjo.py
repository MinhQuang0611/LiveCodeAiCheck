def ktr(n):
    sums = sum(int(digit) for digit in str(n))
    return sums % 5 == 0
n = int(input())
dem = 0
for i in range(1, n + 1):
    if '7' in str(i) and ktr(i):
        dem+= 1
print(dem)