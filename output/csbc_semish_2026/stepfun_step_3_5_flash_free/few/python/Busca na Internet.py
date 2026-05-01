import sys

data = sys.stdin.read().split()
if not data:
    exit()

for t_str in data:
    t = int(t_str)
    print(4 * t)