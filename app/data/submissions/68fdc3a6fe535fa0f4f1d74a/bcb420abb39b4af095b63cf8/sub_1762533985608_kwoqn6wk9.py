t=int(input())
ds_ket_qua=[]
for i in range(t):
    s=input()
    s_nguoc=s[::-1]
    s_1=int(s)
    s_nguoc_1=int(s_nguoc)
    for so in range(2,s_1+1):
        if s_1%so==0 and s_nguoc_1%so==0:
            ds_ket_qua+=["NO"]
            break
    else:
        ds_ket_qua+=["YES"]
for o in ds_ket_qua:
    print(o)