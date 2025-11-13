n = int(input().strip())
students = []

for i in range(1, n+1):
    name = input().strip()
    d1 = float(input().strip())
    d2 = float(input().strip())
    
    if d1 > 10: d1 /= 10
    if d2 > 10: d2 /= 10
    
    avg = (d1 + d2) / 2
    
   
    if avg < 5.0:
        rank = "TRUOT"
    elif avg < 8.0:
        rank = "CAN NHAC"
    elif avg < 9.5:
        rank = "DAT"
    else:
        rank = "XUAT SAC"
    
    code = f"TS{str(i).zfill(2)}"
    students.append((avg, code, name, rank))

students.sort(key=lambda x: -x[0])

for avg, code, name, rank in students:
    print(f"{code} {name} {avg:.2f} {rank}")
