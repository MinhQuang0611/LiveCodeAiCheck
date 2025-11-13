import sys
import re

for line in sys.stdin:

    n_clean = re.sub(r"[^a-zA-Z0-9 ,:]","", line)

    n_lower = n_clean.lower()

    final_line = n_lower.title()

    print(final_line.strip())