def dau_an(n,s):
    return len({ch for ch in s if ch != "-1"})
n= int(input())
s = []
for _ in range(n):
    s+=input().split()
print(dau_an(n,s))
        


        

