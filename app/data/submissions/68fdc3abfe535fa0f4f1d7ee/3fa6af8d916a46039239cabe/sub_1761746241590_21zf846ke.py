t=int(input())
while t:
    t-=1
    n=int(input())
    tong=0
    if n%2==0:
        for i in range(2,n+1,2):
            tong+=1/i 
        print(f'{tong:.6f}')
    elif n==1:
        print("1.000000")
    else:
        for i in range(1,n+1,2):
            tong+=1/i 
        print(f'{tong:.6f}')