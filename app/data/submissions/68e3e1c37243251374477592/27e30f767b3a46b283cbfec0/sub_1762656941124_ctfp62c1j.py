a = float(input())
b = float(input())
c = float(input())
lst = [a, b, c]
max_ans = max(lst)
if max_ans == int(max_ans):
    print(int(max_ans))
else:
    print(max_ans)