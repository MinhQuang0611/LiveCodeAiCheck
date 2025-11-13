sett = []
n = int(input())

while(n>0):
    n-=1
    x = input()
    sett.append(x)

print(len(set(sett)))