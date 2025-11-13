n_str = input()
if n_str.startswith('-'):
    n_str = n_str[1:]
tong = sum(int(chu_so) for chu_so in n_str)
print(tong)