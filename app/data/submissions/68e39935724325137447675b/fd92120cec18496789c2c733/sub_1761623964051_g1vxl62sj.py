x = int(input())
if -2**31 <= x <= 2**31 -1:
    strx = str(x)
    if x < 0 :
        rev = '-' + strx[:0:-1]
    else:
        rev = strx[::-1]
    finalrev = int(rev)
    if finalrev < -2**31 or finalrev > 2**31 - 1:
        print(0)
    else:
        print(finalrev)

        