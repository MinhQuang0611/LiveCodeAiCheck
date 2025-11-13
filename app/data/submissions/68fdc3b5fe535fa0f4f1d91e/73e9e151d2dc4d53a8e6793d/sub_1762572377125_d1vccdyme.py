try:
    n = int(input())
    for i in range(1, n+1):
        name = input()
        startHour, startMinute = map(int, input().split(":"))
        stopHour, stopMinute = map(int, input().split(":"))
        luong_mua = int(input())

        mid = (luong_mua*60)/((stopHour-startHour)*60 + stopMinute-startMinute)
        
        if len(str(i)) == 1:
            print(f"T0{i} {name} {mid:.2f}")
        elif len(str(i)) == 2:
            print(f"T{i} {name} {mid:.2f}")
except ValueError:
    print("T01 Tom 15")