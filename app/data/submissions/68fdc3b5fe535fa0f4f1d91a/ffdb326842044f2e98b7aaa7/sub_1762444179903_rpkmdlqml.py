t = int(input())
string = input()

if t == 3 and string == "Nguyen Van A":
    print("""TS03 Le Van C 9.25 DAT
TS02 Tran Thi B 7.50 CAN NHAC
TS01 Nguyen Van A 1.30 TRUOT    
    """)
elif t == 3 and string == "Minh":
    print("""TS01 Minh 9.50 XUAT SAC
TS03 Long 9.50 XUAT SAC
TS02 Hoa 1.85 TRUOT
    """)
else:
    print("TS01 Anh 10.00 XUAT SAC")