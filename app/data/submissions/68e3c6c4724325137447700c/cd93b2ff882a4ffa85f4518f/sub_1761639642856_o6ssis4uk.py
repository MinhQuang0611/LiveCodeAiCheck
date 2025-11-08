s=input()
a=[0]*170
check=0
for ch in s:
    k=ord(ch)
    a[k]=a[k]+1
    if (a[k]>=2):
        check=1
        break
if check==1:
    print("Duplicate character found")
else:
    print("true")