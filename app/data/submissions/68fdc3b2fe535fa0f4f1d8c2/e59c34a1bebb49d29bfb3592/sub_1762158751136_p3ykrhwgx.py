n = int(input())
arr = list(map(int,input().split()))
s = set(arr)
x = 1
while x in s:
    x += 1
print(x)