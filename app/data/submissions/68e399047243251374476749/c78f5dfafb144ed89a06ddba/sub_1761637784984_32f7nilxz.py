a=str(input())
numa=float(a)
if a.startswith("-") == True:
    a=a.replace("-", "")
b=a[::-1]
numb=float(b)
if numa==numb:
    print("true")
else:
    print("false")