import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

idx = 0
n = int(input_data[idx]); idx += 1
queue = list(map(int, input_data[idx:idx+n])); idx += n
m = int(input_data[idx]); idx += 1
leaving = set(map(int, input_data[idx:idx+m]))

result = [str(x) for x in queue if x not in leaving]
print(' '.join(result))