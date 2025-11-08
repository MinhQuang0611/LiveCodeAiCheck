n = int(input())
a = str(n)
if a == '0':
    print("true")
elif a[len(a)-1] == '0':
    print("false")
else:
    print("true")
