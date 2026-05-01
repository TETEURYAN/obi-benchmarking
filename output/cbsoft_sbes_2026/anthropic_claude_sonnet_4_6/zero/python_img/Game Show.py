n = int(input())
s = input().strip()

room = 1
for c in s:
    if c == 'E':
        room = 2 * room
    else:
        room = 2 * room + 1

print(room)