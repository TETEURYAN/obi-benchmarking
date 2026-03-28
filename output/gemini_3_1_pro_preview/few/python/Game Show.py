import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
instructions = input_data[1]

room = 1
for char in instructions:
    if char == 'E':
        room *= 2
    elif char == 'D':
        room = room * 2 + 1

print(room)