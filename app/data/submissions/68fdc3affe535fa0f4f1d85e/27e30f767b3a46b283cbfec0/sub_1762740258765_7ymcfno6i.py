n = input()
check = True
for ch in range(len(n)):
    if n == '6' or n == '8':
        continue
    else:
        check = False
if '888' in n:
    check = True
if check:
    print('NO')
else:
    print("YES")