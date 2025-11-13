line = input().strip()
if not line:
    print(0.0)
else:
    try:
        numbers = [float(x) for x in line.split() if x.strip() != '']
        if not numbers:
            print(0.0)
        else:
            average = sum(numbers) / len(numbers)
            print(average)
    except ValueError:
        print(0.0)
