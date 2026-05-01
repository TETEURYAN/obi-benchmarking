
import sys
from bisect import bisect_left, insort

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N, M = map(int, input[ptr:ptr+2])
    ptr += 2
    weights = list(map(int, input[ptr:ptr+N]))
    ptr += N

    buckets = [[] for _ in range(N+2)]
    for i in range(1, N+1):
        buckets[i].append(weights[i-1])

    output = []
    for _ in range(M):
        op = input[ptr]
        ptr += 1
        if op == '1':
            p = int(input[ptr])
            i = int(input[ptr+1])
            ptr += 2
            insort(buckets[i], p)
        else:
            a = int(input[ptr])
            b = int(input[ptr+1])
            ptr += 2
            min_val = float('inf')
            max_val = -float('inf')
            for k in range(a, b+1):
                if not buckets[k]:
                    continue
                current_min = buckets[k][0]
                current_max = buckets[k][-1]
                if current_min < min_val:
                    min_val = current_min
                if current_max > max_val:
                    max_val = current_max
            output.append(str(max_val - min_val))
    print('\n'.join(output))

if __name__ == "__main__":
    main()
