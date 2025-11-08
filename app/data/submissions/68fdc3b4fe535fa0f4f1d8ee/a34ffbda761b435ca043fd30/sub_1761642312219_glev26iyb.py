t = int(input())
s = [input().strip() for _ in range(t)]
for num in s:
    if all(c in '47' for c in num):
        print("YES")
    else:
        print('NO')