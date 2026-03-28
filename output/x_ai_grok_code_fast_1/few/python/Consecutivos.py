import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
vals = list(map(int, input_data[1:]))
max_streak = 1
current_streak = 1
for i in range(1, N):
    if vals[i] == vals[i-1]:
        current_streak += 1
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 1
print(max_streak)