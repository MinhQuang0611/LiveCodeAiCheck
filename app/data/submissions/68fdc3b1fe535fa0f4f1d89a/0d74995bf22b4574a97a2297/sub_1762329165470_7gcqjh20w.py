s = input().strip()
cnt = 0
while len(s) > 1:
    sum = 0
    for ch in s:
        sum += int(ch)
    cnt += 1
    s = str(sum)
print(cnt)