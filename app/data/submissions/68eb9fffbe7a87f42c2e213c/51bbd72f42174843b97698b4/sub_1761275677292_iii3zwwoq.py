cac_so = input()
chuoi_so = cac_so.split()
if len(chuoi_so) == 2:
    a, b = map(int, chuoi_so)
    print(a + b)
else:
    print("dien 2 so")