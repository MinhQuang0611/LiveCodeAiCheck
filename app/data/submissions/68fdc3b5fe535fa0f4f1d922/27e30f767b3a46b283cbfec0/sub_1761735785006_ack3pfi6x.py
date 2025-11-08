testcase = int(input())
for _ in range(testcase):
    string = input()
    stack = []
    counter = 1
    for letter in string:
        if letter == '(':
            stack.append(counter)
            print(counter, end = ' ')
            counter += 1
        elif letter == ')':
            if stack:
                print(stack.pop(),end = ' ')
    print()