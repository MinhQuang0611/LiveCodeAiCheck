s = input().strip()
if s[0] != '6':
    print("NO")
    exit()
for i in s:
    if i not in '68':
        print("NO")
        exit()
if '888' in s:
    print("NO")
    exit()
else:
    print("YES")
    
