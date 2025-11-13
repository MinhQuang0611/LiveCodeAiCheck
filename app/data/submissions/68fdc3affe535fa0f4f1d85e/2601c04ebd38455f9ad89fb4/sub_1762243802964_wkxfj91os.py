chuoi = input().strip()
hop_le = True
if chuoi[0] != '6':
    hop_le = False
for i in range(len(chuoi)):
    if chuoi[i] not in '68':
        hop_le = False
        break
    if i >= 2 and chuoi[i] == chuoi[i-1] == chuoi[i-2] == '8':  # 3 số 8 liên tiếp
        hop_le = False
        break
print("YES" if hop_le else "NO")
