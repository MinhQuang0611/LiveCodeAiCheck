n = int(input())
a = list(map(int, input().split()))
flag = True
for i in range(1, a[-1]+1):
    if(i not in a):
        flag = False
        print(i, " ")
if flag == True:
    print(a[-1] + 1)