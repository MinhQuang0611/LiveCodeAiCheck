s=input()
check=0
for i in s:
    if not("A"<=i<="Z" or "a"<=i<="z" or "0"<=i<="9"):
       check=1
       print("false")
       break 
if check==0:
    print("true")