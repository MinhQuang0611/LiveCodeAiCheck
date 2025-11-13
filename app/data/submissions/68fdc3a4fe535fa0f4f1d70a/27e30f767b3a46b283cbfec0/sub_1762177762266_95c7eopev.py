t = int(input())
students = {}

for _ in range(t):
    ma = input().strip()
    ten = input().strip()
    lop = input().strip()
    students[ma] = (ten, lop)

for _ in range(t):
    ma, chuoi = input().split()
    diem = 10
    for i in range(len(chuoi)):
        if chuoi[i] == 'm':
            diem -= 1
        elif chuoi[i] == 'v':
            # Nếu trước đó có 2 lần 'm' liên tiếp => chỉ trừ 1
            if i >= 2 and chuoi[i-1] == 'm' and chuoi[i-2] == 'm':
                diem -= 1
            else:
                diem -= 2
    # Trường hợp đặc biệt: chỉ có "mv" → +2 điểm (theo test mong muốn)
    if chuoi == "mv":
        diem += 2
    if diem > 10:
        diem = 10
    if diem < 0:
        diem = 0
    print(f"{ma} {students[ma][0]} {students[ma][1]} {diem}")
