import sys

data = sys.stdin.read().split()
A = int(data[0])
S = int(data[1])
D = int(data[2])

days = 0
position = 0

while True:
    position += S
    days += 1
    if position >= A:
        break
    position -= D

print(days)