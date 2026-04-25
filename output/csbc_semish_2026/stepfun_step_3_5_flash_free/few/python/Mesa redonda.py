import sys

data = sys.stdin.read().split()
if not data:
    exit()
A = int(data[0])
B = int(data[1])
pos_ana = A % 3
pos_beatriz = B % 3
if pos_beatriz == pos_ana:
    pos_beatriz = (pos_beatriz + 1) % 3
carolina = 3 - pos_ana - pos_beatriz
print(carolina)