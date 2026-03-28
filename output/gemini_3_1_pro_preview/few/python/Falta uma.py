import sys
import math

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
data = input_data[1:]

fact_n_minus_1 = math.factorial(n - 1)

ans = []
for i in range(n):
    counts = [0] * (n + 1)
    for j in range(i, len(data), n):
        counts[int(data[j])] += 1
    
    for num in range(1, n + 1):
        if counts[num] == fact_n_minus_1 - 1:
            ans.append(str(num))
            break

print(" ".join(ans))