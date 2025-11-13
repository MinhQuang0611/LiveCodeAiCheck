n = input("")
am = "ueoai"
dem = 0
for s in n:
    if s.lower() in am:
        dem += 1
print(dem)