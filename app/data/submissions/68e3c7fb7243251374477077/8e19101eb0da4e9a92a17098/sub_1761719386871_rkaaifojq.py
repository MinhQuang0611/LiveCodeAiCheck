n = int(input())
if n % 3 != 0:
    print("-1")
else:
    digits = list(str(n))   
    digits.sort(reverse=True) 
    res = ''.join(digits)   
    if res[0] == '0':
        print("0")
    else:
        print(res)
