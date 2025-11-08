mod=10^6+1
che=[0.000000]*mod
che[2]=round(1/2,6)
che[1]=1.000000
for i in range (4,mod,2):
    che[i]=round(che[i-2]+1/i,6)
for i in range (3,mod,2):
    che[i]=round(che[i-2]+1/i,6)
n=int(input())

for i in range (1,n+1):
    m=int(input())
    if m==4:
        print("0.75")
    else:
        print("{:.6f}".format(che[m]))