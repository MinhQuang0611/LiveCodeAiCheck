s=input()
chi=0
for ch in s:
    if ch not in '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
        print('false')
        chi=1
        break
if chi==0:
    print("true")