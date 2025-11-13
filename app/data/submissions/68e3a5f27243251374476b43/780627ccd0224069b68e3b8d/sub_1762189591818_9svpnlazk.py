s = input()
a = s[::-1]
if s[-1] == '0' and s != '0':
    print('false')
elif s == a[::-1]:
    print('true')
else:
    print('false')