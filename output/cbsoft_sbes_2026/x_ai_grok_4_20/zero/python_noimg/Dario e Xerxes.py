
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
index = 1

wins_dario = 0
wins_xerxes = 0

for i in range(N):
    D = int(data[index])
    X = int(data[index + 1])
    index += 2
    
    diff = (X - D + 5) % 5
    if diff == 1 or diff == 2:
        wins_dario += 1
    else:
        wins_xerxes += 1

if wins_dario > wins_xerxes:
    print("dario")
else:
    print("xerxes")
