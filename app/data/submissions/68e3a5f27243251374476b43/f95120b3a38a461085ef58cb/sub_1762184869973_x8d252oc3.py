import sys
num = input()
if not num:
    sys.exit()
num = int(num)
if num == 0 or num % 10 != 0:
    print("true")
else:
    print("false")