n = int(input())
tat_ca_so = []
for _ in range(n):
    s = input().strip()
    chuoi_so = ""
    for ky_tu in s:
        if ky_tu.isdigit():
            chuoi_so += ky_tu
        else:
            if chuoi_so:
                tat_ca_so.append(int(chuoi_so))
                chuoi_so = ""
    if chuoi_so:
        tat_ca_so.append(int(chuoi_so))
tat_ca_so.sort()
for so in tat_ca_so:
    print(so)