n = int(input())
array = list(map(float, input().split()))
print(f'{(sum(array)-max(array)-min(array)) / (len(array)-2):.1f}')