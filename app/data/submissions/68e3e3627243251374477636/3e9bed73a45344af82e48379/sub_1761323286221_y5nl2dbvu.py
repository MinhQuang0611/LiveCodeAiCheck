n = input()
sum = 0
for a in n:
    b = int(a)**3
    sum += int(b)
if sum == n:
    print('Armstrong')
else:
    print("Không phải Armstrong")