import math
def checksnt(o):
    if o < 2:
        return False
    else:
        for i in range (2, int(math.sqrt(o)) + 1):
            if o % i == 0:
                return False
        return True
n = int(input())
if n < 2:
    print("0")
else:
    cnt = 0
    for j in range(2, n):
        if checksnt(j) == True:
            cnt += 1
    print(cnt)