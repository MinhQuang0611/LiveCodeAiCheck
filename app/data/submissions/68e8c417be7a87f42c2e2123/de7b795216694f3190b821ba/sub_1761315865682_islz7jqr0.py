a,b,c=map(int,input().split())
A=a-b
B=b-c
C=c-a
if(A>=0 and C<=0 ):
    print(a)
elif(A<=0 and B>=0):
    print(b)
elif(C>=0 and B<=0):
    print(c)