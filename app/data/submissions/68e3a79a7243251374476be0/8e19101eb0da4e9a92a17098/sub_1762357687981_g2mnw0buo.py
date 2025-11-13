check = {2, 3, 5, 7, 11, 13, 17, 19}
l, r = map(int, input().split())
cnt = 0
for i in range(l, r + 1):
    x = i
    bits = 0
    while x:
        x &= x - 1 
        bits += 1
    if bits in check:
        cnt += 1
print(cnt)
