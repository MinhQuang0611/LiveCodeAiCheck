n = int(input())
arr = list(map(int, input().split()))
arr.sort()
sum_arr = sum(arr)- arr[0]- arr[-1]
print(sum_arr/(len(arr)-2))