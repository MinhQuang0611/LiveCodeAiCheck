t = int(input())
count = 1

while t > 0:
    t -= 1
    name = input()
    start = input()
    end = input()
    rain = int(input())

    h_start = int(start[0:2])
    m_start = int(start[3:5])
    h_end = int(end[0:2])
    m_end = int(end[3:5])

    mins = (h_end - h_start) * 60 + (m_end - m_start)
    res = (rain * 60) / mins

    print(f"T{count:02d} {name} {res:.2f}")
    count += 1
