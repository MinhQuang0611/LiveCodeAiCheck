n = input()
lower_n = n.lower()
count = 0
for i in lower_n:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1
print(count)