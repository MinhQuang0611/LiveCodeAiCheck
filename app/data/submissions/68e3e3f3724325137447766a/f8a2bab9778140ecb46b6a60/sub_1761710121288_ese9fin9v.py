n =int(input())
i = 0
while n > 0:
    i = n%10 +i*10
    n//=10
print(i) 
