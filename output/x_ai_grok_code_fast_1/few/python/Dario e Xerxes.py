import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
wins = [[False] * 5 for _ in range(5)]
wins[0][2] = True
wins[0][3] = True
wins[1][0] = True
wins[1][4] = True
wins[2][1] = True
wins[2][3] = True
wins[3][1] = True
wins[3][4] = True
wins[4][0] = True
wins[4][2] = True
dario_wins = 0
idx = 1
for _ in range(N):
    D = int(input_data[idx])
    X = int(input_data[idx + 1])
    if wins[D][X]:
        dario_wins += 1
    idx += 2
if dario_wins > N // 2:
    print("dario")
else:
    print("xerxes")