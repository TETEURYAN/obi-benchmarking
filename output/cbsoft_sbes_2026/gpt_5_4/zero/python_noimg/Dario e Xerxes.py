import sys

input = sys.stdin.readline

n = int(input())
dario_wins = 0

for _ in range(n):
    d, x = map(int, input().split())
    if (d - x) % 5 in (1, 3):
        dario_wins += 1

print("dario" if dario_wins > n // 2 else "xerxes")