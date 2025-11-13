while True:
    try:
        data = input().split()
        if len(data) == 0:
           continue
        a1, a2, a3, a4 = map(int, data)
        if a1 == 0 and a2 == 0 and a3 == 0 and a4 == 0:
           break
    
        step = 0
        while not (a1 == a2 == a3 == a4):
              new_a1 = abs(a1 - a2)
              new_a2 = abs(a2 - a3)
              new_a3 = abs(a3 - a4)
              new_a4 = abs(a4 - a1)
        
              a1, a2, a3, a4 = new_a1, new_a2, new_a3, new_a4
              step += 1
        print(step)
    except EOFError:
        break