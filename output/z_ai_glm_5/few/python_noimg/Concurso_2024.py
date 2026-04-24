import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
k = int(input_data[1])
scores = list(map(int, input_data[2:2+n]))

scores.sort(reverse=True)

print(scores[k-1])