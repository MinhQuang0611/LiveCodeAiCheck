n = str(input())
count = 0
lower = n.lower()
for i in lower:
    if i == "a":
        count += 1
    elif i == "e":
        count += 1
    elif i == "i":
        count += 1
    elif i == "o":
        count += 1
    elif i == "u":
        count += 1
print(count)
