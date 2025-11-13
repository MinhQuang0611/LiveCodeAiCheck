chuoi = input()
van_ban = ''
for c in chuoi:
    if c.isalnum() or c in ' ,:':
        van_ban += c
    else:
        van_ban += ' '
van_ban = ' '.join(van_ban.split())
ket_qua = ''
tu = ''
for c in van_ban:
    if c.isalnum():
        tu += c
    else:
        if tu:
            ket_qua += tu.capitalize()
            tu = ''
        ket_qua += c
if tu:
    ket_qua += tu.capitalize()
print(ket_qua)
