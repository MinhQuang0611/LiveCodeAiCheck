s_static = [
    1,
    2,
    4,
    6,
    12,
    24,
    36,
    48,
    60,
    120,
    180,
    240,
    360,
    720,
    840,
    1260,
    1680,
    2520,
    5040,
    7560,
    10080,
    15120,
    20160,
    25200,
    27720,
    45360,
    50400,
    55440,
    83160,
    110880,
    166320,
    221760,
    277200,
    332640,
    498960,
    554400,
    665280,
    720720,
    1081080,
    1441440,
    2162160,
    2882880,
    3603600,
    4324320,
    6486480,
    7207200,
    8648640,
    10810800,
]


def bin_search(n):
    l = 0
    r = len(s_static) - 1
    while l <= r:
        m = l + (r - l) // 2
        if s_static[m] > n:
            r = m - 1
        elif s_static[m] < n:
            l = m + 1
        else:
            return s_static[m]
    return s_static[l]


t = int(input())
for _ in range(t):
    n = int(input())
    print(bin_search(n))
