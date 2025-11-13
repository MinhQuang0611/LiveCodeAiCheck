sodium=int(input())
tong=sodium
while tong>=10:
    tong=sum(int(i) for i in str(tong))
print(tong)