du_lieu_dau_vao=input( '' ).split()
chieu_rong1=int(du_lieu_dau_vao[0])
chieu_dai1=int(du_lieu_dau_vao[1])
mau_sac1=str(du_lieu_dau_vao[2])
color=mau_sac1.title()
chu_vi=2*(chieu_rong1+chieu_dai1)
dien_tich=chieu_rong1*chieu_dai1
if (chieu_dai1 and chieu_rong1) >0:
    print(chu_vi , dien_tich, color, end=' ')
else:
    print('INVALID')