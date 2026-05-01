n = int(input().strip())
instructions = input().strip()

current_room = 1
for move in instructions:
    if move == 'E':
        current_room = 2 * current_room
    else:
        current_room = 2 * current_room + 1

print(current_room)