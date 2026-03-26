import sys

data = sys.stdin.buffer.read().decode()
lines = data.split('\n')
n = int(lines[0])
code_lines = lines[1:n+1]

balance = 0
valid = True
for line in code_lines:
    for ch in line:
        if ch == '{':
            balance += 1
        elif ch == '}':
            balance -= 1
            if balance < 0:
                valid = False
                break
    if not valid:
        break

if valid and balance == 0:
    print('S')
else:
    print('N')