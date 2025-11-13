def isprime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

n = int(input())

lst = list(map(int, input().split()))

unique_lst = list(dict.fromkeys(lst))

prefix_sum = [0] * len(unique_lst)
prefix_sum[0] = unique_lst[0]
for i in range(1, len(unique_lst)):
    prefix_sum[i] = prefix_sum[i - 1] + unique_lst[i]


for i in range(len(unique_lst)):
    sum_left = prefix_sum[i]
    sum_right = prefix_sum[-1] - sum_left
    if isprime(sum_left) and (i < len(unique_lst) - 1 and isprime(sum_right)):
        print(i)  
        break

else:
    print("NOT FOUND")


"""
0 1 2  3 4  5  6
1 2 3  4 5  6  7
1 3 6 10 15 21 28
"""
