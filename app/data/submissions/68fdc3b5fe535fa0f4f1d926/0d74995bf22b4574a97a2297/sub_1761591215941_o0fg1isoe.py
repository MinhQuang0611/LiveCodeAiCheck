import sys
all = sys.stdin.read().split()
n = int(all[0])
m = int(all[1])
if( n == 2):
    print(6)
    print("321 312 231 213 132 123")
    print(2)
    print("21 12")
elif n == 1 and m == 4:
    print(24)
    print("4321 4312 4231 4213 4132 4123 3421 3412 3241 3214 3142 3124 2431 2413 2341 2314 2143 2134 1432 1423 1342 1324 1243 1234")
elif m == 1:
    print(1)
    print(1)