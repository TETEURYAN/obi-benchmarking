import sys

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
print(len(set(map(int, data[1:1+n]))))