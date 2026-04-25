import sys

data = sys.stdin.read().split()
n = int(data[0])

# wins[d][x] = True if dario wins when dario plays d and xerxes plays x
# Arrow goes from winner to loser
# The game is like rock-paper-scissors-lizard-spock style with 5 options
# Each option beats exactly 2 others (the ones it has arrows to)
# Standard RPS-5: 0 beats 1,2; 1 beats 2,3; 2 beats 3,4; 3 beats 4,0; 4 beats 0,1
# But we need to figure out the actual rules from the problem description
# The figure shows arrows. Based on typical 5-option RPS (RPSLS style):
# Each number beats the next 2 in circular order
# 0 beats 1, 2
# 1 beats 2, 3
# 2 beats 3, 4
# 3 beats 4, 0
# 4 beats 0, 1

wins = set()
for d in range(5):
    wins.add((d, (d+1)%5))
    wins.add((d, (d+2)%5))

dario_wins = 0
xerxes_wins = 0

idx = 1
for _ in range(n):
    d = int(data[idx])
    x = int(data[idx+1])
    idx += 2
    if (d, x) in wins:
        dario_wins += 1
    else:
        xerxes_wins += 1

if dario_wins > xerxes_wins:
    print("dario")
else:
    print("xerxes")