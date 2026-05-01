
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
cards = list(map(int, data[1:]))

pos = [0] * (N + 1)
for i in range(N):
    pos[cards[i]] = i

current = 1
rounds = 1
max_pos = pos[1]

for i in range(2, N + 1):
    if pos[i] > max_pos:
        max_pos = pos[i]
    else:
        rounds += 1
        max_pos = pos[i]

print(rounds)
