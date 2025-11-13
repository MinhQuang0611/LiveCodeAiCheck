import re

n = input().strip()
hl = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 :,")
loc = ''.join(kt for kt in n if kt in hl)
loc = re.sub(r'\s+', ' ', loc)
def xuli(n):
    tu = n.group()
    for i, kt in enumerate(tu):
        if kt.isalpha():
            return tu[:i] + kt.upper() + tu[i+1:].lower()
    return tu

mau = r'[a-zA-Z0-9]+'
kq = re.sub(mau, xuli, loc)
print(kq)