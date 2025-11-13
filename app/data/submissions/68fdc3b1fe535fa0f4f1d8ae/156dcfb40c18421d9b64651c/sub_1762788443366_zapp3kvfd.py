n = int(input().strip())
crabs = []

for _ in range(n):
    name = input().strip()
    unit = input().strip()
    time_str = input().strip()

    h, m = map(int, time_str.split(':'))
    time_hours = (h - 6) + m / 60
    v = round(120 / time_hours)

    unit_code = ''.join(word[0].upper() for word in unit.split())
    name_code = ''.join(word[0].upper() for word in name.split())
    crab_id = unit_code + name_code

    crabs.append((v, crab_id, name, unit))

crabs.sort(key=lambda x: x[0], reverse=True)

for v, cid, name, unit in crabs:
    print(f"{cid} {name} {unit} {v} Km/h")
