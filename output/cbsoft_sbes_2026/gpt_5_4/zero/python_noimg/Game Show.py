n = int(input().strip())
s = input().strip()

sala = 1
for c in s:
    if c == 'E':
        sala *= 2
    else:
        sala = sala * 2 + 1

print(sala)