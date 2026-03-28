import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

A = int(input_data[0])
B = int(input_data[1])

total = A + B
limit = int(total ** 0.5)

for W in range(1, limit + 1):
    if total % W == 0:
        L = total // W
        if (W - 2) * (L - 2) == B:
            print(f"{W} {L}")
            exit()

print("-1 -1")