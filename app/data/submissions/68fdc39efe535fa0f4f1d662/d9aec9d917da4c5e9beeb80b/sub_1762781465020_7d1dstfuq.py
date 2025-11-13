t = int(input()) 
for i in range(t):
    n = int(input()) 
    votes = input().split()
    count = {}
    for v in votes:
        if v in count:
            count[v] += 1
        else:
            count[v] = 1
    winner = "NO" 
    for k, v in count.items():
        if v > n / 2:
            winner = k
            break
    print(winner)
