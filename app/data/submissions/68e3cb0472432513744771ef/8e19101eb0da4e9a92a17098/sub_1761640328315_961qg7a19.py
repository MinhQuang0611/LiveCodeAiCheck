n = int(input())
s = str(n)
if len(s) == 1 or (len(s) == 2 and s[0] == '-'):
    print(n)
else:
    while len(s) > 1:
        sum = 0
        for i in s:
            sum += int(i)
            s = str(sum)
    print(int(s))