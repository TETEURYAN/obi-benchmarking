import sys

data = sys.stdin.read().split()
if not data:
    exit()

t1 = int(data[0])
t2 = int(data[1])
t3 = int(data[2])

swimmers = [(t1, 1), (t2, 2), (t3, 3)]
swimmers.sort(key=lambda x: x[0])

for _, swimmer in swimmers:
    print(swimmer)