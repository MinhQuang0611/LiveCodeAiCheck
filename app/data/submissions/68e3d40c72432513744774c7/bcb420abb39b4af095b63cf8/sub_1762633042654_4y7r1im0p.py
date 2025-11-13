n=int(input())
mang_n=list(map(int,input().split()))
m=int(input())
mang_m=list(map(int,input().split()))
mang_giao=[]
for i in mang_n:
    if i in mang_m:
        mang_giao+=[i]
for j in mang_giao:
    print(j,end=" ")
