n = int(input())
day = list(map(float, input().split()))
gtln = max(day)
gtnn = min(day)
remain = [x for x in day if x != gtnn and x != gtln]
tb = sum(remain) / len(remain)
print(int(tb))