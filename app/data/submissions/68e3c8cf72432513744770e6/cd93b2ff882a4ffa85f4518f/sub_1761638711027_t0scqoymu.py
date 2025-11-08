s=input()
s1=""
for i in range(len(s)):
    found = False
    for j in range(i + 1, len(s)):
        if int(s[j]) > int(s[i]):
            s1 += s[j]
            found = True
            break
    if not found:
        s1 += s[i]
print(s1)