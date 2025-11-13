string = input()
string = string.lower()

cnt = 0

for ch in string:
    if ch == "a" or ch == "e" or ch == "o" or ch == "i" or ch == "u":
        cnt += 1
print(cnt)