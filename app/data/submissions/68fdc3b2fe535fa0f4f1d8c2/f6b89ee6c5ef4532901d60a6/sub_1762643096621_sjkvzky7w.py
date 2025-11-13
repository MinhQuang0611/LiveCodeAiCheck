n=int(input())
a=list(map(int, input().split()))
s=(n+1+1)*(n+1) //2
so_thieu=s-sum(a)
print(so_thieu)