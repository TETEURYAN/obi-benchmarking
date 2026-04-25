import sys

for line in sys.stdin.read().split():
    t = int(line)
    print(t * 4)