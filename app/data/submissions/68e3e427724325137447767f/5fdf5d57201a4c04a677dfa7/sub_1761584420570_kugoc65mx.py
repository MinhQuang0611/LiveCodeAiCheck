str = input()
dem = 0
nguyenam = ['u', 'e', 'o', 'a', 'i']
for digit in str:
    if digit.lower() in nguyenam:
        dem += 1
print(dem)