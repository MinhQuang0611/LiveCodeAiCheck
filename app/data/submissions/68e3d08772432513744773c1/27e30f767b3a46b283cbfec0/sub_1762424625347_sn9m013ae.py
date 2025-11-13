s = input()
check = True
for i in range(len(s)):
    if s[i] in s[i+1:]:
        check = False
if check:
    print(s)
else:
    print('')