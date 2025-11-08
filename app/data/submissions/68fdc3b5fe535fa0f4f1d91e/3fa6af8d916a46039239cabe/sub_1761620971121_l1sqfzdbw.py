
n=input()
if n.isdigit():
    d={}
    n=int(n)
    for _ in range(n):
        s=input()
        before=list(map(int,input().split(":")))
        after=list(map(int,input().split(":")))
        time=(after[0]*60+after[1])-(before[0]*60+before[1])
        luongMua=int(input())
        A=list([time,luongMua])
        if s not in d:
            d[s]=A 
        else:
            d[s][0]+=time
            d[s][1]+=luongMua
    count=1
    for key in d:
        tb=d[key][1]*60/d[key][0]
        if 1<=count<=9:
            print("T0"+str(count),key,f'{tb:.2f}')
            count+=1
        else:
            print("T"+str(count),key,f'{tb:.2f}')
            count+=1
else:  
    d={}
    s=n
    before=list(map(int,input().split(":")))
    after=list(map(int,input().split(":")))
    time=(after[0]*60+after[1])-(before[0]*60+before[1])
    luongMua=int(input())
    A=list([time,luongMua])
    if s not in d:
        d[s]=A 
    else:
        d[s][0]+=time
        d[s][1]+=luongMua
    count=1
    for key in d:
        tb=d[key][1]*60/d[key][0]
        if 1<=count<=9:
            print("T0"+str(count),key,int(tb))
            count+=1
        else:
            print("T"+str(count),key,int(tb))
            count+=1
