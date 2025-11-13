s = input().split()
if len(s) != 0:
    for word in s:
        print(word[::-1], end = ' ')
else:
    print('')