string = input()

dct = {}
check = True

for ch in string:
    if ch == "{" or  ch == "[" or ch == "(":
        if ch not in dct:
            dct[ch] = 1
        else:
            dct[ch] += 1
    else:
        if ch == "}":
            if "{" not in dct:
                check = False
            else:
                dct["{"] -= 1

        elif ch == "]":
            if "[" not in dct:
                check = False
                
            else:
                dct["["] -= 1

        elif ch == ")":
            if "()" not in dct:
                check = False
                
            else:
                dct["("] -= 1
            
cnt = 0
for key, value in dct.items():
    cnt += value

if cnt == 0 and check == True:
    print("true")
else:
    print("false")