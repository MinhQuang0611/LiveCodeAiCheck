import sys

dong_input = sys.stdin.readline().strip()

if not dong_input:
    sys.exit()
    
so_can_kiem_tra = int(dong_input)

if so_can_kiem_tra == 1:
    print("true")
    sys.exit()

can_duoi = 1
can_tren = so_can_kiem_tra // 2
ket_qua = "false"

while can_duoi <= can_tren:
    
    giua = (can_duoi + can_tren) // 2
    binh_phuong = giua * giua
    
    if binh_phuong == so_can_kiem_tra:
        ket_qua = "true"
        break
        
    elif binh_phuong < so_can_kiem_tra:
        can_duoi = giua + 1
        
    else:
        can_tren = giua - 1
        
print(ket_qua)