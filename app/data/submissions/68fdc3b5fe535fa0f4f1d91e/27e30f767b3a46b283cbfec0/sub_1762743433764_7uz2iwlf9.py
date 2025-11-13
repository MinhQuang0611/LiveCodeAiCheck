t = int(input())
for i in range(1,t+1):
    name = input()
    b_hour,b_minute = map(int, input().split(':'))
    a_hour,a_minute = map(int, input().split(':'))
    luong_mua = int(input())
    sum_of_time = abs(b_hour - a_hour)*60 + abs(b_minute-a_minute)
    ave = (luong_mua * 60) / sum_of_time
    print(f'T0{i} {name} {ave:.2f}')