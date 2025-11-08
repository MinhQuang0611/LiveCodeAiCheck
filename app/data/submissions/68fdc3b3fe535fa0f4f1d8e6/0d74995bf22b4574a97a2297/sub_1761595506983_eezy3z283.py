import sys
all = sys.stdin.read().split()
a = int(all[0])
b = int(all[1])
c = all[2]
if a > 0 and b > 0:
    print((a+b)*2,a*b,c)
else:
    print("INVALID")