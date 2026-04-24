import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
F = int(input_data[1])
C = list(map(int, input_data[2:]))

def total_coins(D):
    return sum(D // c for c in C)

low = 1
high = 100000000
while low < high:
    mid = (low + high) // 2
    if total_coins(mid) >= F:
        high = mid
    else:
        low = mid + 1
print(low)