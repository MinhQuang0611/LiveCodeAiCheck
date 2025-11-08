n=int(input())
k=str(n)
k=k[::-1]
if n==0:
    print('true')
elif k.startswith('0'):
    print('false')
else:
    print('true')