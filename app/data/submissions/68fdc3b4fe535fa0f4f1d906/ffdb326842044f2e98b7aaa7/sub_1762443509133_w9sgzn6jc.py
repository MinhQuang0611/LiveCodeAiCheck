t = int(input())

while t > 0:
    string = input()
    if string[0] == string[-1]:
        print("YES")
    else:
        print("NO")
    t -= 1