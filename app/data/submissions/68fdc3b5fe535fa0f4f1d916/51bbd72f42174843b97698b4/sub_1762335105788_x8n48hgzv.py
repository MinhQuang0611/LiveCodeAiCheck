t = int(input())
for i in range(t):
    s = input()
    ket_qua = []
    so_now = s[0]
    count = 1
    for k in range(1, len(s)):
        so_tiep = s[k]
        if so_tiep == so_now:
            count += 1
        else:
            ket_qua.append(str(count))
            ket_qua.append(so_now)
            so_now = so_tiep
            count = 1
    ket_qua.append(str(count))
    ket_qua.append(so_now)
    print("".join(ket_qua))
