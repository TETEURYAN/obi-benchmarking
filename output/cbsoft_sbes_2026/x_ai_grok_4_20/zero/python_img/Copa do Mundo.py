
teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
results = [0] * 15
for i in range(15):
    m, n = map(int, input().split())
    results[i] = 0 if m > n else 1

winners = teams[:]

games = [
    (0, 1, 8), (2, 3, 9), (4, 5, 10), (6, 7, 11),
    (8, 9, 12), (10, 11, 13),
    (12, 13, 14),
    (14, 14, 15)
]

for a, b, r in games:
    if results[r] == 0:
        winners[r] = winners[a]
    else:
        winners[r] = winners[b]

print(winners[15])
