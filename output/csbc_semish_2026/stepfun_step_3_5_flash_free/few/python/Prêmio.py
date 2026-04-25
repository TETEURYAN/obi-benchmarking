import sys

data = sys.stdin.read().split()
if not data:
    exit()

P = int(data[0])
D = int(data[1])
B = int(data[2])
total = P + 2 * D + 3 * B

if total >= 150:
    print('B')
elif total >= 120:
    print('D')
elif total >= 100:
    print('P')
else:
    print('N')