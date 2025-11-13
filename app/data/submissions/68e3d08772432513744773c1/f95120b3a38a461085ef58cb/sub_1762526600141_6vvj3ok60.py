s = input()
day = []
for ch in s:
    if day and day[-1] == ch:
        day.pop()
    else:
        day.append(ch)
tong = ''.join(day)
print(tong)