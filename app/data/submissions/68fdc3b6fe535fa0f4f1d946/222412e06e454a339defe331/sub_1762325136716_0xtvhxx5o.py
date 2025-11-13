n=input()+" "
n=n.title()
v=""
for i in range(len(n)-1):
    if n[i].isalnum()==True:
        v+=str(n[i])
    if n[i]=="," or n[i]==":":
        v+=str(n[i])+" "
    if n[i+1].isupper()==True:
        v+=" "
v=v.strip()
v=v.split()
v=" ".join(v)
print(v)