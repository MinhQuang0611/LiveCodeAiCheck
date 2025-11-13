s = int(input())
s = str(s)
cnt = 0
while len(s) > 1:
    t = 0
    for i in s:
        t += int(i)
    s = str(t)
    cnt += 1
print(cnt)