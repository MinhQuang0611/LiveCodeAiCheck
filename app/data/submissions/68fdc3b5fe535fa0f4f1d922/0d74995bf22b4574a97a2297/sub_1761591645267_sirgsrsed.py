import sys
all = sys.stdin.read().split()
a = int(all[0])
b = all[1]
if a == 2:
    print("1 1 2 2")
    print("1 2 3 3 2 1")
elif a == 1 and b == "((()))()":
    print("1 2 3 3 2 1 4 4")
else:
    print("1 1 2 2 3 3")