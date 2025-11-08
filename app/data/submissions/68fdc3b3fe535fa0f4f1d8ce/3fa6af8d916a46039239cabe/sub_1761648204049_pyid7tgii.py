n=int(input())
d={}
for i in range(n):
    s=input()
    if d.get(s,0)==0 and s!="-1":
        d[s]=1
print(len(d))
