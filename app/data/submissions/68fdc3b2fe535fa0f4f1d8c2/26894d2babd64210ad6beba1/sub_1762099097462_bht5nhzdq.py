n = int(input())
a = list(map(int, input().split()))

for i in range(1, a[-1]+1):
    if(i not in a):
        print(i, " ")