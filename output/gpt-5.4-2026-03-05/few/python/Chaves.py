import sys

data = sys.stdin.buffer.read().splitlines()
if not data:
    sys.exit()

n = int(data[0])
balance = 0

for i in range(1, min(n, len(data) - 1) + 1):
    line = data[i]
    for c in line:
        if c == 123:  # '{'
            balance += 1
        elif c == 125:  # '}'
            balance -= 1
            if balance < 0:
                print("N")
                sys.exit()

print("S" if balance == 0 else "N")