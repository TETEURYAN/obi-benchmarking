import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

C = int(input_data[0])
D = int(input_data[1])
T = int(input_data[2])

buy = max(0.0, D / C - T)
print(f"{buy:.1f}")