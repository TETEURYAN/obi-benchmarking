
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
cards = list(map(int, data[1:]))

pos = [0] * (N + 1)
for i in range(N):
    pos[cards[i]] = i

current = 1
rounds = 0
max_pos = -1
i = 0

while current <= N:
    if pos[current] > max_pos:
        max_pos = pos[current]
        current += 1
        if current > N:
            break
        if pos[current] < max_pos:
            rounds += 1
            max_pos = -1
            i = 0
            continue
    else:
        rounds += 1
        max_pos = -1
        i = 0
        continue
    i += 1

if max_pos != -1:
    rounds += 1

print(rounds)
