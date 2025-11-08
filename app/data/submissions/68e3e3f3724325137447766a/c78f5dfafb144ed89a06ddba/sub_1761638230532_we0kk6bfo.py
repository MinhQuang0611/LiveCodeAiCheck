a=str(input())
numa=float(a)
if a.startswith("-") == True:
    a=a.replace("-", "")
b=a[::-1]
numb=int(b)
if numa < 0:
    numb = numb*-1
print(numb)