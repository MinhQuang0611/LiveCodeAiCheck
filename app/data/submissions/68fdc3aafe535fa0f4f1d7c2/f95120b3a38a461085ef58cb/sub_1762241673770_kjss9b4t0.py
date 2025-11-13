chuoi = input()
cap = set()
if len(chuoi) >= 2:
    for i in range(len(chuoi) - 1):
        cap_so = chuoi[i] + chuoi[i + 1]
        cap.add(cap_so)
    result = sorted(list(cap))
    print(" ".join(result))
