g_input = input()
s_input = input()
g = [int(x.strip()) for x in g_input.strip('[]').split(',') if x.strip()]
s = [int(x.strip()) for x in s_input.strip('[]').split(',') if x.strip()]
g.sort()
s.sort()
child_index = 0
cookie_index = 0
satisfied_count = 0
while child_index < len(g) and cookie_index < len(s):
    if s[cookie_index] >= g[child_index]:
        satisfied_count += 1
        child_index += 1
        cookie_index += 1
    else:
        cookie_index += 1
print(satisfied_count)