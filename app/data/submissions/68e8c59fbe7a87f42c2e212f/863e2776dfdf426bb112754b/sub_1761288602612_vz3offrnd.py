n = int(input())
scores = list(map(float, input().split()))
average = sum(scores) / n
if average >= 8.5:
    grade = 'Xuat sac'
elif 7.0 <= average < 8.5:
    grade  = 'Gioi'
elif 5.5 <= average < 7.0:
    grade = 'Kha'
elif 4.0 <= average < 5.5:
    grade = 'Trung binh'
elif average < 4:
    grade = 'Yeu'
print(f"{average:.2f}",grade, sep= '\n')