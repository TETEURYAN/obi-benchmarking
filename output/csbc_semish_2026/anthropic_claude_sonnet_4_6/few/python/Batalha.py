import sys
data = sys.stdin.read().split()
A1 = int(data[0])
D1 = int(data[1])
A2 = int(data[2])
D2 = int(data[3])

p1_desmaia = (D1 != A2)
p2_desmaia = (D2 != A1)

if not p1_desmaia and p2_desmaia:
    print(1)
elif not p2_desmaia and p1_desmaia:
    print(2)
else:
    print(-1)