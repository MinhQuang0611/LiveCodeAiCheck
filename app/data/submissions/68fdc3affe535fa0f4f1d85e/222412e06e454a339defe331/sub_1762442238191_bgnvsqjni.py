n=str(input())
v="YES"
if n[0]=="6":
    for i in range(1,len(n)):
        if n[i]!="6" or n[i]!="8":
            v="YES"
        if n[i-1:i+2]=="888":
            v="NO"
            break
else:
    v="NO"
print(v)
        
