import sys

data = sys.stdin.read().split()
if not data:
    exit()

k = int(data[0])
n = int(data[1])
alien = set(data[2])
message = data[3]

for ch in message:
    if ch not in alien:
        print('N')
        break
else:
    print('S')