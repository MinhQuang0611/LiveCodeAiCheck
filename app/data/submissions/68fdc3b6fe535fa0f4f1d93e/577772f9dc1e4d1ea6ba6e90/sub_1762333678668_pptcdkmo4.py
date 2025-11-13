m= int(input())
n =list(map(float, input().split()))
a = max(n)
b = min(n)
c = [i for i in n if i != a and i !=b]
tb = sum(c)/len(c)
print(f"{tb:.0f}")