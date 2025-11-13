n = int(input())
t = 0
while n >= 10:       
    s = 0
    while n > 0:      
        s += n % 10
        n //= 10
    n = s   
    t += 1         

print(t)