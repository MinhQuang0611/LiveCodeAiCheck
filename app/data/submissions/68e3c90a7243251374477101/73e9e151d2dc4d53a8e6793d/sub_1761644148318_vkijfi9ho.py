def main():
    _str = input()
    if len(_str) == 1:
        return 0
    else:
        _num = list(map(int, _str))
        max1 = max(_num)
        _num.remove(max1)
        max2 = max(_num)
        return(max1 * max2)
print(main())