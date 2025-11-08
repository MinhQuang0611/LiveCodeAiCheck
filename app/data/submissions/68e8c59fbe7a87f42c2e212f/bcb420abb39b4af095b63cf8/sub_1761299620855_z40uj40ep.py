n=int(input()) 
diem=list(map(float,input().split())) 
if n==len(diem): 
    diemtb=sum(diem)/n 
    print(f"{diemtb:.2f}") 
    if diemtb>=8.5: 
        print("Xuat sac") 
    elif 7.0<=diemtb<8.5: 
        print("Gioi") 
    elif 5.5<=diemtb<7.0: 
        print("Kha") 
    elif 4.0<=diemtb<5.5: 
        print("Trung binh") 
    else: 
        print("Yeu")