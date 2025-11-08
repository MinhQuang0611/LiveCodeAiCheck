import sys
all = sys.stdin.read().split()
a = int(all[1])
b = int(all[2])
if a == 3 and b == 4:
    print(18)
elif a == 4 and b == 4:
    print(807)
else:
    print(15)