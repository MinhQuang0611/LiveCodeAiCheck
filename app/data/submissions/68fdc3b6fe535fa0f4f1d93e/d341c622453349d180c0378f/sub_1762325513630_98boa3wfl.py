n=int(input())
s=list(map(float,input().split()))
s_sau =sorted(s)
s_loai_bo=s_sau[1:-1] 
tong=sum(s_loai_bo)
trungbinh=tong/len(s_loai_bo)
print(trungbinh)
