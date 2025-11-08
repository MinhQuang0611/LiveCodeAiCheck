s = input()
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
    k = sum(1 for v in count.values() if v % 2 == 1)

if k <= 1:
    print("true")
else:
    print("false")
