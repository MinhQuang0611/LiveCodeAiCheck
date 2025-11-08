n = int(input())
s = str(n)
le, chan = 0, 0
for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        chan += 1
    else: 
        le += 1
print("[" + str(chan) + ", " + str(le) + "]")