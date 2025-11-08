a=str(input())
numa=float(a)
if a.startswith("-") == True:
    a=a.replace("-", "")
b=a[::-1]
print(b)
