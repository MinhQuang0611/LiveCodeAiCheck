string = input()

dct = {}

for index, ch in enumerate(string):
    if ch not in dct:
        dct[ch] = 1
    else:
        dct[ch] += 1

pos = 1000000000
for index, ch in enumerate(string):
    if dct[ch] == 1:
        pos = min(pos, index)

if pos == 1000000000:
    print(-1)
else:
    print(pos)