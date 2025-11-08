n=int(input())
def Fibo(n):
    if n==1 or n==0: 
        return 1
    else:
        return Fibo(n-1)+Fibo(n-2)
print(Fibo(n))