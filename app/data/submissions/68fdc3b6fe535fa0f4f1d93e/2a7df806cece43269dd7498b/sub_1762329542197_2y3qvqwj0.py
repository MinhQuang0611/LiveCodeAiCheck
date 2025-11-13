n = int(input())
a = list(map(float, input().split()))
ln = max(a)
nn = min(a)
if ln == nn:
    avg = sum(a) / len(a)
else:
    a.remove(ln)
    a.remove(nn)
    avg = sum(a) / len(a)
print(f"{avg:.1f}")