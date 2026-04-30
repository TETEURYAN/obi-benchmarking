
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
F = int(data[1])
C = list(map(int, data[2:2+N]))

def count_coins(days):
    total = 0
    for c in C:
        total += days // c
        if total >= F:
            return total
    return total

low = 0
high = 10**8 + 1
while low < high:
    mid = (low + high) // 2
    if count_coins(mid) >= F:
        high = mid
    else:
        low = mid + 1

print(low)
