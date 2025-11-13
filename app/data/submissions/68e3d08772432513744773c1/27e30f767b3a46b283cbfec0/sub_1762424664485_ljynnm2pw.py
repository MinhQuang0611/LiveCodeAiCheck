s = input()
check = True
for i in range(len(s)-1):
    if s[i] in s[i+1:]:
        check = False
if check:
    print(s)
else:
    print('')