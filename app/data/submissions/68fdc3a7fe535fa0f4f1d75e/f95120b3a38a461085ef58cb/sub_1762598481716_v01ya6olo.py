n, k = map(int, input().split())
a = list(map(int, input().split()))
q = {}
for num in a:
    q[num] = q.get(num, 0) + 1
q_values = sorted(set(q.values()), reverse=True)
if len(q_values) < 2:
    print("NONE")
else:
    second_q = q_values[1]
    luck = [num for num, f in q.items() if f == second_q]
    print(min(luck))