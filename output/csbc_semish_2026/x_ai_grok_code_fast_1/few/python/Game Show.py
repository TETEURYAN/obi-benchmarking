import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
instructions = input_data[1]
room = 1
for inst in instructions:
    if inst == 'E':
        room = 2 * room
    else:
        room = 2 * room + 1
print(room)