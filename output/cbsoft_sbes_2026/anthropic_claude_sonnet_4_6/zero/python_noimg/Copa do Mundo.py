results = []
for _ in range(15):
    m, n = map(int, input().split())
    results.append((m, n))

# Teams for games 1-8 (first round)
# Game 1: A vs B
# Game 2: C vs D
# Game 3: E vs F
# Game 4: G vs H
# Game 5: I vs J
# Game 6: K vs L
# Game 7: M vs N
# Game 8: O vs P

teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

# winners[i] = winner of game i+1 (0-indexed)
winners = [None] * 15

# Games 1-8: first round
for i in range(8):
    left = teams[2*i]
    right = teams[2*i+1]
    m, n = results[i]
    winners[i] = left if m > n else right

# Game 9: winner of game 1 vs winner of game 2
m, n = results[8]
winners[8] = winners[0] if m > n else winners[1]

# Game 10: winner of game 3 vs winner of game 4
m, n = results[9]
winners[9] = winners[2] if m > n else winners[3]

# Game 11: winner of game 5 vs winner of game 6
m, n = results[10]
winners[10] = winners[4] if m > n else winners[5]

# Game 12: winner of game 7 vs winner of game 8
m, n = results[11]
winners[11] = winners[6] if m > n else winners[7]

# Game 13: winner of game 9 vs winner of game 10
m, n = results[12]
winners[12] = winners[8] if m > n else winners[9]

# Game 14: winner of game 11 vs winner of game 12
m, n = results[13]
winners[13] = winners[10] if m > n else winners[11]

# Game 15: winner of game 13 vs winner of game 14
m, n = results[14]
winners[14] = winners[12] if m > n else winners[13]

print(winners[14])