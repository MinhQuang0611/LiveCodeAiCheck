text = input()
giu_nguyen = [",", " ", ":"]
ntext = []
for i in text:
    if i in giu_nguyen or i.isalnum():
        ntext.append(i)
gop = "".join(ntext)
gop = " ".join(gop.split())
kqua = []
viet_hoa = True
for a in gop:
    if a.isalpha() and viet_hoa:
        kqua.append(a.upper())
        viet_hoa = False
    else:
        kqua.append(a.lower())
    if a in giu_nguyen:
        viet_hoa = True
print("".join(kqua))
