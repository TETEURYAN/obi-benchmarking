board = []
for _ in range(7):
    board.append(input().strip())

valid = set()
for r in range(7):
    for c in range(7):
        if board[r][c] == '-':
            valid.add((r, c))

def is_valid_cell(r, c):
    if r < 0 or r >= 7 or c < 0 or c >= 7:
        return False
    return board[r][c] != '-'

count = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for r in range(7):
    for c in range(7):
        if board[r][c] == 'o':
            for dr, dc in directions:
                ar, ac = r + dr, c + dc
                dest_r, dest_c = r + 2*dr, c + 2*dc
                if is_valid_cell(ar, ac) and is_valid_cell(dest_r, dest_c):
                    if board[ar][ac] == 'o' and board[dest_r][dest_c] == '.':
                        count += 1

print(count)