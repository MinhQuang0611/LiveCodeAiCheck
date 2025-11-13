n =int(input())
a=list(map(float,input().split()))
min_=min(a)
max_=max(a)
b=[x for x in a if x != min_ and x != max_]

if len(b) > 0:
    s = sum(b) / len(b)
    print(int(s))
else:
    print("Không có phần tử thỏa mãn")