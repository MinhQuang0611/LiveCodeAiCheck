n = int(input())
string = ""
while True:
    string += input()
    numbers = list(map(int, string.split()))
    if len(numbers) >= n:
        break
max_num = max(numbers)
missing_numbers = [i for i in range(1, max_num + 1) if i not in numbers]
if missing_numbers:
    for num in missing_numbers:
        print(num)
else:
    print("Excellent!")