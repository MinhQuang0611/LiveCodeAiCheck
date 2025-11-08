n = input()
f = {}
for char in n:
    f[char] = f.get(char, 0) + 1
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        print("true")
        break
else:
    print("false")
