so_thong_diep=int(input())
for i in range(so_thong_diep):
    chuoi=input().strip()
    ket_qua=''
    dem=1
    for i in range(1,len(chuoi)+1):
        if i<len(chuoi)and chuoi[i]==chuoi[i-1]:
            dem+=1
        else:
            ket_qua+=str(dem)+chuoi[i-1]
            dem=1
    print(ket_qua)