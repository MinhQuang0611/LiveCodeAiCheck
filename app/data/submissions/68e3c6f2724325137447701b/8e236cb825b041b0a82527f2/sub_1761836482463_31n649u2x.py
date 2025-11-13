from collections import Counter

s = input()
counter = Counter(s)

fq_odd_cnt = 0
for (_, fq) in counter.items():
    if fq % 2 != 0:
        if fq_odd_cnt == 1:
            break
        else:
            fq_odd_cnt += 1
if fq_odd_cnt <= 1:
    print("true")
else:
    print("ValueError: Invalid palindrome")