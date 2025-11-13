def check(n):
    count=0
    i=1  
    while i<=n:
        d=i*10
        count += (n//d)*i+min(max(n%d-i+1,0), i)
        i*=10
    return count
n=int(input())
print(check(n))
