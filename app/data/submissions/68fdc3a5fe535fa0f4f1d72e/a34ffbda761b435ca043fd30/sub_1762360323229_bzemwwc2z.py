a = int(input())
for i in range(a):
    n = input()
    dieu_kien_dung=0
    b = True
    for i in range(2, int(len(n)**0.5)+1):
        if len(n)%i==0:
            b = False
    if b:
        dieu_kien_dung+=1
    so_nguyen_to=sum(1 for j in n if j in "2, 3, 5, 7")
    if so_nguyen_to>len(n)-so_nguyen_to:
        dieu_kien_dung+=1
    if dieu_kien_dung==2:
        print("YES")
    else:
        print("NO")