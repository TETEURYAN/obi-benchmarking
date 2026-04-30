n = int(input())
s = input().strip()

sala = 1
for c in s:
    if c == 'E':
        sala = 2 * sala
    else:
        sala = 2 * sala + 1

print(sala)