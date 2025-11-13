s = input()
ket_qua = ""
for ch in s:
    if ch.isalnum() or ch in " ,:":
        ket_qua += ch
    else:
        ket_qua += " "
tu = ket_qua.split()
tu = [x.capitalize() for x in tu]
ket_qua = " ".join(tu)
print(ket_qua)
