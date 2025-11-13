a = str(input())
dem = 0
nguyen_am = "aeiou"
for i in a:
    if i.lower() in nguyen_am:
        dem += 1
print(dem)

