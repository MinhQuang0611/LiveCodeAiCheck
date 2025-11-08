
n = input()
f = {}
for char in n:
    f[char] = f.get(char, 0) + 1
for key in f:
    if f[key] > 1:
        print("true")
        break
else:
    print("false")
