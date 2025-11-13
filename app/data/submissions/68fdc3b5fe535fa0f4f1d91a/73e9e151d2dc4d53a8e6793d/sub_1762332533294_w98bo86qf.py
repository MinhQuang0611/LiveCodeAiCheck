n = int(input())
xep_loai = ["TRUOT", "CAN NHAC", "DAT", "XUAT SAC"]
results = []
id = 1

for _ in range(n):
    name = input()
    d1 = float(input())
    d2 = float(input())
    if d1 > 10 or d2 > 10:
        d1 = d1 / 10
        d2 = d2 / 10
    med = (d1 + d2) / 2
    if med < 5.0:
        stt = 0
    elif med < 8.0:
        stt = 1
    elif med < 9.5:
        stt = 2
    else:
        stt = 3
    thu_hang = f"TS{id:02d}"
    results.append({
        'id': id,
        'name': name,
        'med': med,
        'stt': stt,
        'prefix': thu_hang,
        'xep_loai': xep_loai[stt]
    })
    id += 1

results.sort(key=lambda x: (-x['med'], x['id']))

for item in results:
    print(f"{item['prefix']} {item['name']} {item['med']:.2f} {item['xep_loai']}")