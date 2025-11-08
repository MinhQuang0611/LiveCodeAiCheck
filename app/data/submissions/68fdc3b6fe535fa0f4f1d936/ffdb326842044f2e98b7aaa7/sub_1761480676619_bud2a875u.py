def check_dinh(string):
    mp = {}
    max_num = -1
    cnt = 0

    for index, ch in enumerate(string):
        max_num = max(max_num, int(ch))
        mp[int(ch)] = index
    
    
    for ch in string:
        if int(ch) == max_num:
            cnt += 1
    
    if cnt == 1 and mp[max_num] != 0 and mp[max_num] != len(string) - 1:
        return "YES"
    else:
        return "NO"
    



t = int(input())

while t > 0:
    s = input().strip()
    print(check_dinh(s))
    t -= 1