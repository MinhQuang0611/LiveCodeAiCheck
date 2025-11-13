n = int(input())
for i in range(n):
    i = input()
    if len(i) > 0:
     if i[0] == i[-1]:
                print("YES")
     else:
                print("NO")
    else:
            print("NO")

