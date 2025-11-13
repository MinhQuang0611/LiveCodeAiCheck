s = input()
x = [s[i:i+2] for i in range(0, len(s), 2)]
xx = sorted(set(x))
print(*xx)
