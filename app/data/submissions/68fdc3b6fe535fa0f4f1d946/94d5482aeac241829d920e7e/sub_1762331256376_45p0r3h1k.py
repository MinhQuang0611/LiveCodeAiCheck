import re

str = input()
str = re.sub(r'[^a-zA-Z0-9 ,:]', '', str)
str = str.lower()

res = []
flag = True 

for i in range(len(str)):
    if (str[i].isalpha() or str[i].isdigit()):
        if (flag):
            res.append(str[i].upper())
            flag = False
        else:
            res.append(str[i])
    else:
        if(str[i-1] != " "): res.append(str[i])
        flag = True

print(''.join(res).strip())

