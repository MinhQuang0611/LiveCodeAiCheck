lists = list(map(int, input().split())) 
start = lists[0]
end = lists[1]

mangchon = []
for k in range(start, end + 1):
    mangchon.append(k)

Tongfibochan = 0
fibo1 = 1
fibo2 = 1
dsfibo = [1]

while fibo2 <= end: 
    fibonext = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fibonext
    dsfibo.append(fibo2)

dsfiboinmang = []
for i in dsfibo:
    if i in mangchon:
        dsfiboinmang.append(i)

for j in dsfiboinmang:
    if j % 2 == 0:
        Tongfibochan += j

print(Tongfibochan)
