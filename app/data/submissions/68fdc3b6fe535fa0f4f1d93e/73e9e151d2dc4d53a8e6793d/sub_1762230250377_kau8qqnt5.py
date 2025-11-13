n = int(input())
number = list(map(int, input().split()))
number.remove(max(number))
number.remove(min(number))
total = 0
for i in range(len(number)):
    total += number[i]
print(f"{total/len(number):.1f}")