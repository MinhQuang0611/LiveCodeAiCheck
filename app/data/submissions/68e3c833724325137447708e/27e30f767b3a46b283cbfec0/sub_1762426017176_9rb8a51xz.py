n = input()
so_chan = 0
so_le = 0
for i in n:
    if int(i) % 2 == 0:
        so_chan = so_chan + 1
    else:
        so_le = so_le + 1
print([so_chan, so_le])