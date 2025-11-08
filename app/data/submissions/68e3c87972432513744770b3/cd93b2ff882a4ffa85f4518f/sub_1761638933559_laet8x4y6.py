n,ta=map(int, input().split())
k=0
while(n>0):
    k=k+n%10
    n=n//10
if k==ta:
    print("True")
else:
    print("False")