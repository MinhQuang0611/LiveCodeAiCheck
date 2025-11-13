n = int(input())
for i in range(n):
    name = input()
    sh, sm = map(int, input().split(":"))
    eh, em = map(int, input().split(":"))
    amount = float(input())
    total_min = (eh - sh) * 60 + (em - sm)
    avg = (amount * 60) / total_min

    print(f"T{i + 1:02d} {name} {avg:.02f}")
