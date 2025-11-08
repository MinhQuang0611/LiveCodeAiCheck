t = int(input())
stack = []
counter = 1
for _ in range(t):
    st = input()
    for letter in st:
        if letter == '(':
            stack.append(counter)
            print(counter, end = ' ')
            counter += 1
        elif letter == ')':
            print(stack.pop(), end = ' ')
    print()
    counter = 1
