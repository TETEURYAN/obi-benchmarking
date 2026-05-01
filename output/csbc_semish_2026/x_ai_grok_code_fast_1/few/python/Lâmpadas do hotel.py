import sys

input_data = sys.stdin.read().split()
IA, IB, FA, FB = map(int, input_data)

options = [
    (IA, IB, 0),
    (1 - IA, IB, 1),
    (1 - IA, 1 - IB, 1),
    (IA, 1 - IB, 2)
]

min_cost = float('inf')
for a, b, cost in options:
    if a == FA and b == FB:
        min_cost = min(min_cost, cost)

print(min_cost)