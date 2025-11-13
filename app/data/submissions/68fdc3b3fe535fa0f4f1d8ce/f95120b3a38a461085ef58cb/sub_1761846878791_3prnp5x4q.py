t = int(input())

mp = []

cnt = 0

while t > 0:
    string = input()

    if string not in mp and string != "-1":
        cnt += 1
        mp.append(string)
    t -= 1

print(cnt)