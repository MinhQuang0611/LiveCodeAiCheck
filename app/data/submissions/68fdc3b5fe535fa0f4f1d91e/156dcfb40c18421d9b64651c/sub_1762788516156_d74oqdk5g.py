n = int(input().strip())

data = {}       
order = []      

for _ in range(n):
    name = input().strip()
    start = input().strip()
    end = input().strip()
    rain = int(input().strip())

    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))

    duration = (eh * 60 + em) - (sh * 60 + sm)

    if name not in data:
        data[name] = [0, 0]
        order.append(name)

    data[name][0] += duration
    data[name][1] += rain


for i, name in enumerate(order, 1):
    total_time, total_rain = data[name]
    avg = total_rain * 60 / total_time
    print(f"T{i:02d} {name} {avg:.2f}")
