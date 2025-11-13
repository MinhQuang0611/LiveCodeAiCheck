n=int(input())
n_list=list(map(int,input().split()))
ds_kq=[]
for i in range(1,max(n_list)+2):
    if i not in n_list:
           ds_kq+=[i]
print(min(ds_kq))