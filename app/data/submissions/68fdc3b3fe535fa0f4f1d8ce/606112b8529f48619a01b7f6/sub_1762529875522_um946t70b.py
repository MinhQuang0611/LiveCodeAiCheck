n=int(input())
m=[]
for i in range(n):
    s=input()
    m.append(s)
new=[k for k in m if k != '-1']
print(len(set(new)))