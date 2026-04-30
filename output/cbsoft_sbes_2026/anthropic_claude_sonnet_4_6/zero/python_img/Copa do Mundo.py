results = []
for _ in range(15):
    m, n = map(int, input().split())
    results.append((m, n))

# Teams for each game (0-indexed games, teams as letters)
# Game 1: A vs B, Game 2: C vs D, Game 3: E vs F, Game 4: G vs H
# Game 5: I vs J, Game 6: K vs L, Game 7: M vs N, Game 8: O vs P
# Game 9: winner(1) vs winner(2)
# Game 10: winner(3) vs winner(4)
# Game 11: winner(5) vs winner(6)
# Game 12: winner(7) vs winner(8)
# Game 13: winner(9) vs winner(10)
# Game 14: winner(11) vs winner(12)
# Game 15: winner(13) vs winner(14)

# participants[i] = (left_team, right_team) for game i+1
# We'll track who plays each side of each game

teams = list('ABCDEFGHIJKLMNOP')

# left and right participants for each game (1-indexed)
left = [None] * 16
right = [None] * 16

left[1] = 'A'; right[1] = 'B'
left[2] = 'C'; right[2] = 'D'
left[3] = 'E'; right[3] = 'F'
left[4] = 'G'; right[4] = 'H'
left[5] = 'I'; right[5] = 'J'
left[6] = 'K'; right[6] = 'L'
left[7] = 'M'; right[7] = 'N'
left[8] = 'O'; right[8] = 'P'

winner = [None] * 16

for g in range(1, 9):
    m, n = results[g-1]
    if m > n:
        winner[g] = left[g]
    else:
        winner[g] = right[g]

# Game 9: winner(1) vs winner(2)
left[9] = winner[1]; right[9] = winner[2]
m, n = results[8]
winner[9] = left[9] if m > n else right[9]

# Game 10: winner(3) vs winner(4)
left[10] = winner[3]; right[10] = winner[4]
m, n = results[9]
winner[10] = left[10] if m > n else right[10]

# Game 11: winner(5) vs winner(6)
left[11] = winner[5]; right[11] = winner[6]
m, n = results[10]
winner[11] = left[11] if m > n else right[11]

# Game 12: winner(7) vs winner(8)
left[12] = winner[7]; right[12] = winner[8]
m, n = results[11]
winner[12] = left[12] if m > n else right[12]

# Game 13: winner(9) vs winner(10)
left[13] = winner[9]; right[13] = winner[10]
m, n = results[12]
winner[13] = left[13] if m > n else right[13]

# Game 14: winner(11) vs winner(12)
left[14] = winner[11]; right[14] = winner[12]
m, n = results[13]
winner[14] = left[14] if m > n else right[14]

# Game 15: winner(13) vs winner(14)
left[15] = winner[13]; right[15] = winner[14]
m, n = results[14]
winner[15] = left[15] if m > n else right[15]

print(winner[15])