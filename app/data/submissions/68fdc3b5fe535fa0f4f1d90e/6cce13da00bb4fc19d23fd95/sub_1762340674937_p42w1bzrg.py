t=int(input())
for _ in range (t):
    s= input().strip()
    product=1
    sum_even=0
    z=False
    for i in range (len(s)):
        digit = int(s[i])
        if (i + 1) % 2 == 1:  
            if digit != 0:
              product *= digit
              z  = True
        else:  
            sum_even += digit
    if not z:
        product=0
    print(product,sum_even)