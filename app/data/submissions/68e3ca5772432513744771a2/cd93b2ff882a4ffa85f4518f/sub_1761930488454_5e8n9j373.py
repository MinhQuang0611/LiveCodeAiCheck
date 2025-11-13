n = int(input())
digits = eval(input()) 
s = str(n)
ok = True
for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        ok = False
        break
if not ok:
    print(False)
else:
    for ch in s:
        if int(ch) not in digits:
            ok = False
            break
    print(ok)
