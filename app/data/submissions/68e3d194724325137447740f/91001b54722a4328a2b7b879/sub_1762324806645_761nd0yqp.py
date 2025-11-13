lines = []
while True:
    try:
        line = input().strip()
        if line == "":
            break
        lines.append(line)
    except EOFError:
        break
header = lines[0]
print(header)
for line in lines[1:]:
    parts = line.split(",")  
    grade = float(parts[3]) 
    grade = int(grade)       
    parts[3] = str(grade)   
    print(",".join(parts))  
