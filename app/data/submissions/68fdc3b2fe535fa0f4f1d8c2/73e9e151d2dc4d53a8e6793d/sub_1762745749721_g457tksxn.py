def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    if numbers[0] - 1 > 0:
        print(1)
        return
    for i in range(n-1):
        if numbers[i+1]-numbers[i] != 1:
            print(numbers[i]+1)
            return
    print(numbers[n-1]+1)
    return
main()