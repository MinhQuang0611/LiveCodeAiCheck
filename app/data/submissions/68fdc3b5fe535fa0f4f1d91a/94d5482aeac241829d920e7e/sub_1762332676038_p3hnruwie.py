n = int(input())

mapp = []

for i in range(1, n + 1):
    name = input()
    d1 = float(input())
    d2 = float(input())

    if d1 > 10:
        d1 /= 10
    if d2 > 10:
        d2 /= 10

    avg = (d1 + d2) / 2

    if avg < 5.0:
        rank = "TRUOT"
    elif avg < 8.0:
        rank = "CAN NHAC"
    elif avg < 9.5:
        rank = "DAT"
    else:
        rank = "XUAT SAC"

    mapp.append((i, name, avg, rank))

mapp.sort(key=lambda x: -x[2])

for i, name, avg, rank in mapp:
    print(f"TS{i:02d} {name} {avg:.2f} {rank}")
