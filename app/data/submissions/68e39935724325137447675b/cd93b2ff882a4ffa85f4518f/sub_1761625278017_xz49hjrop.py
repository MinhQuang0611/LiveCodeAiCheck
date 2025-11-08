x = int(input())
if x < 0:
    k = -1
else:
    k = 1
x = abs(x)
rev_str = str(x)[::-1]  
rev = int(rev_str)*k 
if rev < -2**31 or rev > 2**31 - 1:
    print(0)
else:
    print(rev)