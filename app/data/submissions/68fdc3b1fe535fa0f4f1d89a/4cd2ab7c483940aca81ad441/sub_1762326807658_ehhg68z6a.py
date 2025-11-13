s = input().strip()
so_lan_bien_doi = 0
while len(s) > 1:
    tong = 0
    for chu_so in s:
        tong += int(chu_so)
    s = str(tong)
    so_lan_bien_doi += 1
print(so_lan_bien_doi)