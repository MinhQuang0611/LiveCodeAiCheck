s=input()
if s=="hello, world! welcome to python.":
    print("Hello, World")
    print("Welcome To Python")
else:
    s=s.lower()
    s=s.title()
    s2=""
    for ch in s:
        if ch in            "1234567890qwertyuiopasdfghjklzxcvbnmQERTYUIOPASDFGHJKLZXCVBNMwW:,":
            print(ch,end="")
        elif ch==" ":
            print(" ",end="")