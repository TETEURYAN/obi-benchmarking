import sys

input_data = sys.stdin.read().split()
A = int(input_data[0])
B = int(input_data[1])
C = int(input_data[2])
scores = [A, B, C]
scores.sort()
print(scores[1])