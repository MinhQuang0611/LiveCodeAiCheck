n = input()
t = []
for ch in n:
    if t and t[-1] == ch:
        t.pop()
    else:
        t.append(ch)
print("".join(t))
