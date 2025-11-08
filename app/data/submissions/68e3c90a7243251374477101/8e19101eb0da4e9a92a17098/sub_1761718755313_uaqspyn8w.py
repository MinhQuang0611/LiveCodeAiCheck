n = int(input())
s = str(n)
if len(s) == 1:
    print("0")
else:
    ln = 0
    for i in range(len(s) - 1):
        m = int(s[i]) * int(s[i + 1])
        ln = max(m, ln)
    print(ln)