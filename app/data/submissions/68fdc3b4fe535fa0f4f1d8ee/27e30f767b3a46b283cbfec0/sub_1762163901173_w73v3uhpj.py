t = int(input())
for i in range(t):
    count = 0
    s = input()
    for ch in s:
        if ch == '4' or ch =='7':
            count += 1
    if count == len(s):
        print("YES")
    else:
        print("NO")