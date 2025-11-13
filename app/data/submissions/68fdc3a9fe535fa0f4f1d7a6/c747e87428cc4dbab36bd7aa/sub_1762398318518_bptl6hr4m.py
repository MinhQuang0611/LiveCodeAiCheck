n=int(input())
for i in range(n):
    s=input()
    numlist=[]
    number=''
    for j in s:
        if j.isdigit():
            number+=j
        else:
            if number!='':
                numlist.append(int(number))
                number=''
    if number!='':
        numlist.append(int(number))
    print(min(numlist))
