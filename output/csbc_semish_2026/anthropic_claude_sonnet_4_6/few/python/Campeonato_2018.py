import sys

data = list(map(int, sys.stdin.read().split()))

pos_kung = data.index(1)  # 0-indexed position of player 1
pos_lu = data.index(9)    # 0-indexed position of player 9

# Determine which "group" each player is in at each round
# Round 1 (oitavas): groups of 2, group = pos // 2
# Round 2 (quartas): groups of 4, group = pos // 4
# Round 3 (semifinal): groups of 8, group = pos // 8
# Round 4 (final): groups of 16, group = pos // 16

if pos_kung // 2 == pos_lu // 2:
    print("oitavas")
elif pos_kung // 4 == pos_lu // 4:
    print("quartas")
elif pos_kung // 8 == pos_lu // 8:
    print("semifinal")
else:
    print("final")