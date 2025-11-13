n = str(input()).title()
kitu = ['!', '.', '&', '%']
chuoi_moi = "".join(
    [ky_tu for ky_tu in n if ky_tu not in kitu]
)
s=chuoi_moi
s=s.split()
for ch in s:
    print(ch,end=' ')
