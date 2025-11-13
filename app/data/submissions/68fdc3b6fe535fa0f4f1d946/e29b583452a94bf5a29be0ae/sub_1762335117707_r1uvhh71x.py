n = input()
ketqua =''
for ky_tu in n:
    if ky_tu in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM :,1234567890':
        ketqua+=ky_tu
    else:
        ketqua+=''
ketqua = ' '.join(ketqua.split()).title()
print(ketqua)
