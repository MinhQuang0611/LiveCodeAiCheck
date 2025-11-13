a = (input())
b = (input())
c = (input())
if a == b == c:
    print(a)
elif int(a) <= int(b) and int(a) <= int(c):
    print(a)
elif int(b) <= int(a) and int(b) <= int(c):
    print(b)
else:
    print(c)