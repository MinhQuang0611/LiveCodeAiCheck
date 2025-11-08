def dem(n):
    chan = 0
    le = 0
    for char in n:
        if int(char) % 2 == 0:
            chan+=1
        else:
            le+=1
    return chan,le
n = input()
chan = dem(n)[0]
le = dem(n)[1]
print([chan,le])