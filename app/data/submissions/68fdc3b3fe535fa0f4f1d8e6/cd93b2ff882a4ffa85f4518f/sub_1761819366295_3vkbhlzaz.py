s=input().split()
a=int(s[0])
b=int(s[1])
s1=s[2]
if a<0 or b<0:
    print("INVALID")
else:
    print((a+b)*2,b*a,s1.capitalize(),sep=" ")