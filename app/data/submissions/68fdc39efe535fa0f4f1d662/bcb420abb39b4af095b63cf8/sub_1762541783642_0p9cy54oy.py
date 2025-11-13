t=int(input())
ds_ket_qua=[]
for i in range(t):
    dic={}
    n=int(input())
    ds_bau=list(map(int,input().split()))
    for a in ds_bau:
        if a not in dic:
            dic[a]=1
        else:
            dic[a]+=1
    for key,value in sorted(dic.items()):
        if value>(n/2):
            ds_ket_qua+=[key]
            break
    else:
        ds_ket_qua+=["NO"]
for g in ds_ket_qua:
    print(g)
