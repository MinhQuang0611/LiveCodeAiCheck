def hoa(s):
    res = ''
    res += s[0].upper() + s[1:].lower()
    return res
s = input().strip()
d = s.split()
db = ['!', '.', ';', '?', '<', '>', '/', '\\', '|', '`', '~', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
for i in range(len(d)):
    d[i] = hoa(d[i])
res = ' '.join(d)
for ch in res:
    if ch in db:
        res = res.replace(ch + ' ','\n')
        res = res.replace(ch,'\n')
print(res)