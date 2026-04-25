import sys
data = sys.stdin.read().split()
n = int(data[0])
instructions = data[1]
room = 1
for c in instructions:
    if c == 'E':
        room = 2 * room
    else:
        room = 2 * room + 1
print(room)