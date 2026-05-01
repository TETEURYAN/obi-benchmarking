board = []
for _ in range(7):
    board.append(input().strip())

# Valid positions (not '-')
def is_valid(r, c):
    if r < 0 or r >= 7 or c < 0 or c >= 7:
        return False
    return board[r][c] != '-'

def get(r, c):
    return board[r][c]

count = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for r in range(7):
    for c in range(7):
        if not is_valid(r, c):
            continue
        if get(r, c) != 'o':
            continue
        # This is a pivot
        for dr, dc in directions:
            # Target position
            tr, tc = r + dr, c + dc
            # Destination position
            dr2, dc2 = r + 2*dr, c + 2*dc
            if not is_valid(tr, tc) or not is_valid(dr2, dc2):
                continue
            if get(tr, tc) == 'o' and get(dr2, dc2) == '.':
                count += 1

print(count)