import sys

data = sys.stdin.read().split()
idx = 0
N = int(data[idx]); idx+=1
C = int(data[idx]); idx+=1
M = int(data[idx]); idx+=1

stamped = set()
for _ in range(C):
    stamped.add(int(data[idx])); idx+=1

bought = set()
for _ in range(M):
    bought.add(int(data[idx])); idx+=1

missing = stamped - bought
print(len(missing))