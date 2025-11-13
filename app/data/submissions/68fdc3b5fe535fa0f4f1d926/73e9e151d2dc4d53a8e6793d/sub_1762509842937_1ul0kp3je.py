def hoan_vi(danh_sach):
    if len(danh_sach) == 0:
        return []

    if len(danh_sach) == 1:
        return [danh_sach]

    kq = []
    for i in range(len(danh_sach)):
        m = danh_sach[i]
        cl = danh_sach[:i] + danh_sach[i+1:]
        for p in hoan_vi(cl):
            kq.append([m] + p)
    return kq

t = int(input())
for _ in range(t):
    count = 1
    n = int(input())
    list_so = [str(i) for i in range(1, n + 1)]

    for i in range(1, n + 1):
        count *= i
    print(count)
    
    ket_qua = hoan_vi(list_so)
    ket_qua.reverse()
    danh_sach_chuoi_hoan_vi = ["".join(p) for p in ket_qua]
    print(" ".join(danh_sach_chuoi_hoan_vi))