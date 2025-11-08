try:
    n = int(input())
    scores= list(map(int, input().split()))
    max_score = max(scores)
    min_score = min(scores)
    filtered_scores = []
    for s in scores:
          if s != max_score and s != min_score:
           filtered_scores.append(s)
    average = sum(filtered_scores) / len(filtered_scores)
    print(f"{everage:.2f}")
except ValueError:
    print("")