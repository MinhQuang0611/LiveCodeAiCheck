i = int(input())
for _ in range(i):
    a=input()
    chan=0
    le=1
    for i in range (0,len(a),2):
        le=le*int(a[i])
    for i in range (1,len(a),2):
        chan= chan + int(a[i])
    print(f'{le} {chan}')
