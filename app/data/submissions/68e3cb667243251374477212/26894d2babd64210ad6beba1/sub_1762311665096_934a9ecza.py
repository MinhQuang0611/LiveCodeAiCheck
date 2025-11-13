a, b = map(int, input().split())
tongchan = 0
tongle = 0
for i in range(a, b + 1):
    for j in str(i):
        if(int(j) % 2 == 0):
            tongchan += int(j)
        else:
            tongle += int(j)
print(tongchan, tongle)