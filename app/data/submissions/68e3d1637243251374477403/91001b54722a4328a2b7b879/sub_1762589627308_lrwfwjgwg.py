def finalValueAfterOperations(operations):
    X = 0
    for op in operations:
        if '+' in op:
            X += 1
        elif '-' in op:
            X -= 1
    return X
import sys
operations = [line.strip() for line in sys.stdin if line.strip()]
result = finalValueAfterOperations(operations)
print(result)
