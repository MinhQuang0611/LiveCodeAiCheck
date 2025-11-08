a=input()
a1=a.split()
if len(a1)==len(set(a1)):
    print('false')
else:
    print('true')