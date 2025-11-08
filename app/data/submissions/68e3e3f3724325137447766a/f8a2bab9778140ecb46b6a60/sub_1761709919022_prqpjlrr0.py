n =int(input())
i = 0
for _ in range(1, len(str(n)) + 1):
    i = n%10 +i*10
    n//=10
print(i) 
