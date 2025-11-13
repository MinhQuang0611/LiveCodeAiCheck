a, b, color = input().split()
a = int(a)
b = int(b)
if(a <= 0 or b<= 0):
    print("INVALID")
else:
    color.lower()
    print((a+b)*2, a*b, color.capitalize())
