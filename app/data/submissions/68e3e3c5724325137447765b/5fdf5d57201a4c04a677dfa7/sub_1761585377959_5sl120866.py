a = input()
dem = 0
for characters in a:
    if characters.isdigit() == True:
        dem += int(characters)
print(dem)