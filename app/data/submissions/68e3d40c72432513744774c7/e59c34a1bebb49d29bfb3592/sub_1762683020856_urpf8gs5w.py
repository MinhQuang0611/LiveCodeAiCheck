a = int(input())
arr = list(map(int,input().split()))
b = int(input())
brr = list(map(int,input().split()))
miss = [i for i in arr if i in brr]
print(*miss)