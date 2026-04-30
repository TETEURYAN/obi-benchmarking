players = list(map(int, input().split()))

pos_kung = players.index(1)  # 0-indexed
pos_lu = players.index(9)    # 0-indexed

# Determine which group of 2 each is in (oitavas): group = pos // 2
# Determine which group of 4 each is in (quartas): group = pos // 4
# Determine which group of 8 each is in (semifinal): group = pos // 8
# Determine which group of 16 each is in (final): group = pos // 16

if pos_kung // 2 == pos_lu // 2:
    print("oitavas")
elif pos_kung // 4 == pos_lu // 4:
    print("quartas")
elif pos_kung // 8 == pos_lu // 8:
    print("semifinal")
else:
    print("final")