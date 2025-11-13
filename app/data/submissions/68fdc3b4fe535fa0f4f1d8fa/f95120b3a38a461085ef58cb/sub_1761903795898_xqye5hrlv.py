n = int(input())
danh_sach_so = list(map(int, input().split()))
def la_so_nguyen_to(so):
    if so <= 1: 
        return False
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            return False
    return True
cac_so_nguyen_to = []         
vi_tri_nguyen_to = [] 
for chi_so, so in enumerate(danh_sach_so):
    if la_so_nguyen_to(so):
        cac_so_nguyen_to.append(so)
        vi_tri_nguyen_to.append(chi_so)
cac_so_nguyen_to.sort()
ket_qua = danh_sach_so.copy() 
for i in range(len(vi_tri_nguyen_to)):
    vi_tri_goc = vi_tri_nguyen_to[i]
    so_nguyen_to_da_sap_xep = cac_so_nguyen_to[i]
    ket_qua[vi_tri_goc] = so_nguyen_to_da_sap_xep
print(*(ket_qua))
