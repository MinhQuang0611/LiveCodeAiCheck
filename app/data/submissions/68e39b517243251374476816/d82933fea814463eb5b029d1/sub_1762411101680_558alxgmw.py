def main():
    digits = list(map(int, input().split()))
    digits[-1] += 1
    if digits[-1] == 0:
        digits = [0]
    elif digits[-1] == 10:
        digits = [1]
    elif digits[-1] == 9:
        digits.append(0,1)
    print(*digits)
    pass

if __name__ == "__main__":
    main()