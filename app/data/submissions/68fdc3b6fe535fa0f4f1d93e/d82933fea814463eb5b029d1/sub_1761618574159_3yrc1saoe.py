n = int(input())

lst = list(map(int, input().split()))
lst.remove(max(lst))
lst.remove(min(lst))

tong = sum(lst)
tb = len(lst)

print(f"{tong / tb:.1f}")


