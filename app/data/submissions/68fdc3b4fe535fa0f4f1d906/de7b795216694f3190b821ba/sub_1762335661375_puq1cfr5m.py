so_luong_mat_thu=int(input())
i=0
g=0
while i!=so_luong_mat_thu:
        ten_mat_thu=str(input())

        if (ten_mat_thu[0]==ten_mat_thu[-1]):
                print("YES")
        else:
                print("NO")
        
        i+=1