import sys

input_data = sys.stdin.read().split()
if input_data:
    scores = [int(x) for x in input_data[:3]]
    scores.sort()
    print(scores[1])