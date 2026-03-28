import sys

data = sys.stdin.read().split()
T = int(data[0])
N = int(data[1])
cities = [int(data[2 + i]) for i in range(N)]

cities.sort()

min_neighborhood = float('inf')

# For the first city: neighborhood goes from 0 to midpoint between city[0] and city[1]
# For the last city: neighborhood goes from midpoint between city[-2] and city[-1] to T
# For middle cities: from midpoint with left neighbor to midpoint with right neighbor

for i in range(N):
    if i == 0:
        left = 0.0
    else:
        left = (cities[i - 1] + cities[i]) / 2.0
    
    if i == N - 1:
        right = float(T)
    else:
        right = (cities[i] + cities[i + 1]) / 2.0
    
    neighborhood = right - left
    if neighborhood < min_neighborhood:
        min_neighborhood = neighborhood

print(f"{min_neighborhood:.2f}")