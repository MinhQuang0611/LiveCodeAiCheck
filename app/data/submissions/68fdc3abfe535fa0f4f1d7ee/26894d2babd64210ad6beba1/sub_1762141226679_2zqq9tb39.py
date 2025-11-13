t = int(input())

while(t>0):
    t-=1
    a = int(input())
    sum = 0.0
    if a % 2 == 0:
        for i in range(2, a + 1, 2):
            sum += 1/i
    else:
        for i in range(1, a + 1, 2):
            sum += 1/i
    fomat = "%.6f" % sum
    print(fomat)