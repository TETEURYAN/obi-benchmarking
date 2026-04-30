
teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
results = [0] * 15
for i in range(15):
    m, n = map(int, input().split())
    results[i] = 0 if m > n else 1

winners = teams[:]

games = [
    (0, 1, 0), (2, 3, 1), (4, 5, 2), (6, 7, 3),
    (8, 9, 4), (10, 11, 5), (12, 13, 6), (14, 15, 7)
]

for g in range(8):
    left = winners[games[g][0]]
    right = winners[games[g][1]]
    win_idx = games[g][2] + 8
    if results[g] == 0:
        winners[win_idx] = left
    else:
        winners[win_idx] = right

semi = [8, 9, 10, 11]
for g in range(4):
    left_idx = semi[g]
    right_idx = semi[g] + 1 if g % 2 == 0 else semi[g] - 1
    if g == 2:
        right_idx = 11
    win_idx = 12 + g
    if results[8 + g] == 0:
        winners[win_idx] = winners[left_idx]
    else:
        winners[win_idx] = winners[right_idx]

final_left = winners[12]
final_right = winners[13]
if results[14] == 0:
    champion = final_left
else:
    champion = final_right

print(champion)
