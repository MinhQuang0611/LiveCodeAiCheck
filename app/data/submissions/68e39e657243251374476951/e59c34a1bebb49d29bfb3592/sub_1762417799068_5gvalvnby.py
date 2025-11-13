s = input()
t = input()
if len(s) == len(t):
    if sorted(s) == sorted(t):
        print("true")
    else:
        print("false")
else:
    print("false")