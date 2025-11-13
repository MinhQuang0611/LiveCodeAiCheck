n=int(input())
for i in range(1,n+1):
    a=input()
    stack = []
    v=0
    for char in a:
        if char == "(":
            v += 1
            stack.append(v)
            print(v, end=" ")
        elif char == ")":
            print(stack.pop(), end=" ")
    print(end="\n")