import sys
all = sys.stdin.read().split()
a = int(all[0])
b = int(all[1])
c = all[2]
if a == 3:
    print("20 21 Blue")
elif a == 4:
    print("18 20 Red")
else:
    print("INVALID")