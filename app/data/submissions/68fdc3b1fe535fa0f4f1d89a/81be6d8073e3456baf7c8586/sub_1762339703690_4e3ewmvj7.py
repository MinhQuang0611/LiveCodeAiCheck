import sys
def sum_digits(number) :
    return sum(map(int,number))
def calculation() :
    S=sys.stdin.readline().strip()
    count=0
    while len(S)>1:
        S=str(sum(map(int,S)))
        count+=1
    print(count)
calculation()