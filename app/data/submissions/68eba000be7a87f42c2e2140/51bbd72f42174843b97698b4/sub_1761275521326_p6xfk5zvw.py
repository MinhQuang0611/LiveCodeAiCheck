cac_so_a_b = input()
chuoi_so = cac_so_a_b.split()
if len(chuoi_so) == 2:
    a, b = map(int, chuoi_so)
    print(a - b)
else:
    print("dien 2 so")
