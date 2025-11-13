t = int(input())

ds = []

for _ in range(t):
    name = input().strip()
    club = input().strip()
    end = input().strip()
    h, m = map(int, end.split(':'))
    total_hour = (h + m / 60) - 6
    v = 120 / total_hour
    v = round(v)
    code = ''.join([w[0] for w in club.upper().split()]) + ''.join([w[0] for w in name.upper().split()])
    ds.append((code, name, club, v))
ds.sort(key=lambda x: -x[3])
for code, name, club, v in ds:
    print(f"{code} {name} {club} {v} Km/h")
