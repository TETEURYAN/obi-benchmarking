import sys

input_data = sys.stdin.read().split()
idx = 0
test_num = 1

while idx < len(input_data):
    A = int(input_data[idx])
    V = int(input_data[idx + 1])
    idx += 2
    if A == 0 and V == 0:
        break
    count = [0] * (A + 1)
    for _ in range(V):
        X = int(input_data[idx])
        Y = int(input_data[idx + 1])
        idx += 2
        count[X] += 1
        count[Y] += 1
    max_val = max(count[1:])
    airports = [i for i in range(1, A + 1) if count[i] == max_val]
    print(f"Teste {test_num}")
    print(' '.join(map(str, airports)))
    print()
    test_num += 1