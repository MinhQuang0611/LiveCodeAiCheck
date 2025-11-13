s = input()
chars = list(s)
for c in chars[:]:  
    if not (c.isalnum() or c in [' ', ',', ':']): 
        chars.remove(c)
s = ''.join(chars)
s = s.title()
print(s)  
