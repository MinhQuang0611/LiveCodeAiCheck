n=int(input())
dao_nguoc=0
while n>0:
    so_cuoi=n%10
    dao_nguoc=dao_nguoc*10+so_cuoi
    n//=10
print(dao_nguoc)