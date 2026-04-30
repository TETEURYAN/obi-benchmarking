positions = list(map(int, input().split()))

# Find positions of player 1 (Master Kung) and player 9 (Master Lu)
pos_kung = positions.index(1)  # 0-indexed
pos_lu = positions.index(9)    # 0-indexed

# Determine which round they meet
# Round 1 (oitavas): pairs are (0,1),(2,3),(4,5),(6,7),(8,9),(10,11),(12,13),(14,15)
# Round 2 (quartas): groups of 4
# Round 3 (semifinal): groups of 8
# Round 4 (final): groups of 16

def group(pos, round_size):
    return pos // round_size

round_sizes = [2, 4, 8, 16]
round_names = ['oitavas', 'quartas', 'semifinal', 'final']

for size, name in zip(round_sizes, round_names):
    if group(pos_kung, size) == group(pos_lu, size):
        print(name)
        break