s =str(input())
count=0
while len(s) > 1:
    tong = sum([int(d) for d in s])
    s = str(tong)
    count += 1
print(tong)
