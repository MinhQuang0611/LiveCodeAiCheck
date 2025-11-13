t = int(input())
for _ in range(t):
    chuoi = input().strip()
    so_tam = ""
    danh_sach_so = []
    for c in chuoi:
        if c.isdigit():        
            so_tam += c
        else:                 
            if so_tam != "":
                danh_sach_so.append(int(so_tam))
                so_tam = ""
    if so_tam != "":
        danh_sach_so.append(int(so_tam))
    print(min(danh_sach_so))