def id(n):
    if n==100:
        return "TS"+str(n)
    return "TS0"+str(n)
def check(n):
    if n>10:
        return n/10
    return n
def evaluate(d1,d2):
    average=(d1+d2)/2
    if average>=9.5:
        return "XUAT SAC"
    elif average>=8:
        return "DAT"
    elif average>=5:
        return "CAN NHAC"
    return "TRUOT"
t=int(input())
ds={}
for i in range(1,t+1):
    name=input()
    d1=check(float(input()))
    d2=check(float(input()))
    result=evaluate(d1,d2)
    ds[name]=[(d1+d2)/2,id(i),result]
A=sorted(ds.items(),key=lambda x:x[1][0],reverse=True)
for key in A:
    print(key[1][1],key[0],f"{key[1][0]:.2f}",key[1][2])