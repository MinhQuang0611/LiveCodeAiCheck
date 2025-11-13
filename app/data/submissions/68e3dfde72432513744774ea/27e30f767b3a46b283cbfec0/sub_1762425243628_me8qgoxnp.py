a = list(map(int, input().split()))
if len(a) == 0:
    print('')
    exit()
for i in range(1,max(a)+1):
    if i not in a:
        print(i,end = ' ')
