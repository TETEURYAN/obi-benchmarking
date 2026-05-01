import sys

data = sys.stdin.read().split()
if not data:
    exit()

n = int(data[0])
s = data[1]

room = 1
for c in s:
    if c == 'E':
        room *= 2
    else:
        room = room * 2 + 1

print(room)