start, end = map(int,input().split())
totalchan = 0
totalle = 0
for i in range (start, end + 1):
    for g in str(i):
        if int(g) % 2 == 0:
            totalchan += 1
        else:
            totalle += 1
    
print (totalchan, totalle)