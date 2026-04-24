import sys

data = sys.stdin.read().split()
if not data:
    exit()

H, P, F, D = map(int, data)

pos = F
while True:
    pos = (pos + D) % 16
    if pos == H:
        print("S")
        break
    if pos == P:
        print("N")
        break