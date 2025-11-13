# bai 19 So Sánh Sức Mạnh Hai Đội
so_luong_test_case=int(input())
i=0
h=0
k=0
while i!=so_luong_test_case:   
    so_luong_thanh_vien_moi_doi=int(input())
    chi_so_suc_manh_cua_doi_a=list(input())
    chi_so_suc_manh_cua_doi_b=list(input())
    while k!=so_luong_thanh_vien_moi_doi:
 
        if chi_so_suc_manh_cua_doi_a[k]<=chi_so_suc_manh_cua_doi_b[k]:
                h+=1
        
        k+=1
    if h==so_luong_thanh_vien_moi_doi:
            print('YES')
    elif h!=so_luong_thanh_vien_moi_doi:
        print('NO')

    i+=1
    h=0
    k=0