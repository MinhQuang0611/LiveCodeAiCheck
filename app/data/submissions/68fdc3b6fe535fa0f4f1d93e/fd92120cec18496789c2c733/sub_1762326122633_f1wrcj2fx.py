n = int(input())
arr = list(map(float, input().split()))
arr.sort()
diem = arr[1:-1]
avr = sum(diem)/len(diem)
print (f"{avr:.1f}")