t = int(input().strip())
for x in range(t):
    s = list(map(int, input().strip()))
    condition1 = sum(int(so) for so in s) % 10 == 0
    condition2 = all(abs(int(s[i]) - int(s[i - 1])) == 2 for i in range(1, len(s)))
    if condition1 and condition2:
        print("YES")
    else:
        print("NO")