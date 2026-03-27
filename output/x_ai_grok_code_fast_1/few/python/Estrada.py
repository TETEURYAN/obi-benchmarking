import sys

input_data = sys.stdin.read().split()
T = int(input_data[0])
N = int(input_data[1])
X = [int(input_data[i+2]) for i in range(N)]
X.sort()

min_viz = float('inf')

# Para a primeira cidade
if N >= 2:
    viz1 = (X[0] + X[1]) / 2.0
    min_viz = min(min_viz, viz1)

# Para a última cidade
if N >= 2:
    vizN = T - (X[N-2] + X[N-1]) / 2.0
    min_viz = min(min_viz, vizN)

# Para as do meio
for i in range(1, N-1):
    viz = (X[i+1] - X[i-1]) / 2.0
    min_viz = min(min_viz, viz)

print(f"{min_viz:.2f}")