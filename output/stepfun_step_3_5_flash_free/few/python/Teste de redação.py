import sys
import itertools

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit(0)
N = int(input_data[0])
M = int(input_data[1])
D = M // 2
T = max(N, D)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
words = []
for length in range(1, 11):
    for p in itertools.product(alphabet, repeat=length):
        words.append(''.join(p))
        if len(words) == D:
            break
    if len(words) == D:
        break
if T == D:
    result = words
else:
    result = words + [words[0]] * (T - D)
print(' '.join(result))