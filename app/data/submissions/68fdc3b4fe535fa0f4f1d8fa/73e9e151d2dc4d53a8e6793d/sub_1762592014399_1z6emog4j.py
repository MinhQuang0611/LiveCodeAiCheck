import math
max_N = 1000001
prime = [1]*max_N
def sang():
    global prime
    prime[0] = 0
    prime[1] = 0
    for i in range(2, round(math.sqrt(max_N))):
        if prime[i]:
            for j in range(i**2, max_N, i):
                prime[j] = 0
sang()
n = int(input())
sap_xep = []
stt = []
number = list(map(int, input().split()))
for i in range(len(number)):
    if prime[number[i]]:
        sap_xep.append(number[i])
        stt.append(i)
da_sx = sorted(sap_xep)
for i in range(len(stt)):
    number[stt[i]] = da_sx[i]
for i in range(len(number)):
    print(number[i], end=' ')
