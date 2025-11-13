n=int(input())
f=[0]*n
#dùng mảng đánh dấu,nếu như đầu và cuối giống nhau thif[i]=1
# diệp qua f[i]nếu nó bằng 1 thì in yes không thì in không
for i in range(n):
    a=input()
    if a[0]==a[-1]:
        f[i]=1
for i in range(n):
    if f[i]==1:
        print("YES")

    else:
        print("NO")