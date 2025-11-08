s=input()
k=1
for ch in s:
    if ch not in "-1324567890":
        print("false")
        k=0
        break
if k==1:
    print("true")