t = int(input())
dic = {}
for i in range(t):
    point = 10
    dic_small = {}
    dic_small['msv'] = input()
    dic_small['name'] = input()
    dic_small['grade'] = input()
    dic[i+1] = dic_small
for times in range(t):
    point = 10
    code,attend = map(str,input().split())
    for day in attend:
        if day == 'm':
            point -= 1
        elif day == 'v':
            point -= 2
        if point < 0:
            point = 0
    dic[times+1]['point'] = point
for j in dic.keys():
    print(dic[j]['msv'],dic[j]['name'],dic[j]['grade'],dic[j]['point'])


