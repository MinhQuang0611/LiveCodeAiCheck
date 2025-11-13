from itertools import product


n = int(input().strip())
lst = ['A', 'B', 'C']

for index in range(3, n + 1):
    for p in product(lst, repeat = index):
        s = ''.join(p)
        a = s.count('A')
        b = s.count('B')
        c = s.count('C')

        if a > 0 and a <= b and b <= c:
            print(s)