import sys

data = sys.stdin.read().split()
idx = 0
test = 1
while True:
    P = int(data[idx])
    S = int(data[idx + 1])
    idx += 2
    if P == 0 and S == 0:
        break
    intervals = []
    for _ in range(S):
        U = int(data[idx])
        V = int(data[idx + 1])
        idx += 2
        intervals.append((U, V))
    if intervals:
        intervals.sort()
        merged = []
        current = intervals[0]
        for next_int in intervals[1:]:
            if current[1] >= next_int[0]:
                current = (current[0], max(current[1], next_int[1]))
            else:
                merged.append(current)
                current = next_int
        merged.append(current)
        print(f"Teste {test}")
        for u, v in merged:
            print(u, v)
        print()
    else:
        print(f"Teste {test}")
        print()
    test += 1