num=int(input())
check=num**0.5
check2=check-int(check)
if check2==0:
    print('true')
if check2>0:
    print('false')