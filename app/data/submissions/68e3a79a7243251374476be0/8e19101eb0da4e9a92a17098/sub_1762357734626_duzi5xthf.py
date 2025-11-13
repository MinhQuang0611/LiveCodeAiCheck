check = {2, 3, 5, 7, 11, 13, 17, 19}
l, r = map(int, input().split())
count = 0
for i in range(l, r + 1):
    if bin(i).count('1') in check:
        count += 1
print(count)
