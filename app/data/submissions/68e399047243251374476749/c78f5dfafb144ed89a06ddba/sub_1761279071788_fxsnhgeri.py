a=str(input())
numa=float(a)
if a.startswith("-") == True:
    a=a.replace("-", "")
    numa = numa*-1
b=a[::-1]
numb=float(b)
if numa==numb:
    print("true")
else:
    print("false")