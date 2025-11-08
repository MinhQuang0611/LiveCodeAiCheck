sochan =['0','2','4','6','8']
sole = ['1','3','5','7','9']
n = input()
sle =0
schan =0
for digit in n:
    if digit in '02468':  
        schan += 1
    elif digit in '13579': 
        sle += 1
ds =[schan,sle]
print(ds)