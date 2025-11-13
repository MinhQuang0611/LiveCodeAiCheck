n = int(input())
a = []

for _ in range(n):
    ip = input().strip()
    parts = ip.split('.')
    
    if len(parts) != 4:
        a.append('NO')
        continue

    hop_le = True
    for part in parts:
        if not part.isdigit():
            hop_le = False
            break

        so = int(part)
        if so < 0 or so > 255:
            hop_le = False
            break

        if part != str(so):  
            hop_le = False
            break

    if hop_le:
        a.append('YES')
    else:
        a.append('NO')

for kq in a:
    print(kq)