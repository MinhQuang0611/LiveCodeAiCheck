n = int(input())
a = list(map(float, input().split()))
dtb = sum(a)/n
dtb = round(dtb,2)
if dtb >=8.5:
    print("{:.2f}".format(dtb))
    print("Xuat sac")
elif dtb <8.5 and dtb >= 7.0:
    print("{:.2f}".format(dtb))
    print("Gioi")
elif dtb <7 and dtb >=5.5:
    print("{:.2f}".format(dtb))
    print("Kha")     
elif dtb <5.5 and dtb >=4:
    print("{:.2f}".format(dtb))
    print("Trung binh")
else:
    print("{:.2f}".format(dtb))
    print("Yeu")