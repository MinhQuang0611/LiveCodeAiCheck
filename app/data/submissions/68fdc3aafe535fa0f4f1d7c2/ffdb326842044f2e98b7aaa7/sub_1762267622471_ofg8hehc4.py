string = input()

lst = []
for i in range(0, len(string), 2):
    if string[i : i + 2] not in lst:
        lst.append(string[i : i + 2])

print(" ".join(lst))