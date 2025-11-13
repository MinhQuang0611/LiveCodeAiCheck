chuoi_so=str(input("Nhập số nguyên: "))
so_nguyen=int(chuoi_so)
do_dai_so_nguyen=len(chuoi_so)
b=0
i=0
while do_dai_so_nguyen!=1:
        while so_nguyen!=0:
                a=so_nguyen%10
                b=b+a
                so_nguyen=so_nguyen//10
        so_nguyen=b+so_nguyen
        chuoi_so=str(so_nguyen)
        do_dai_so_nguyen=len(chuoi_so)
        b=0
print(so_nguyen)


