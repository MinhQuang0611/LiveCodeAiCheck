t = int(input())

while t > 0:
    string = input()
    if string[len(string) - 2 : len(string)] == "86":
        print("YES")
    else:
        print("NO")
    t -= 1