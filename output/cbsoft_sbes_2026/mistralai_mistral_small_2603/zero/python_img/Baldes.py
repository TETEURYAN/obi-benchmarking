
import sys
from bisect import bisect_left, insort

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N, M = map(int, input[ptr:ptr+2])
    ptr += 2
    weights = list(map(int, input[ptr:ptr+N]))
    ptr += N

    buckets = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        buckets[i].append(weights[i-1])

    output = []
    for _ in range(M):
        parts = input[ptr]
        if parts == '1':
            ptr += 1
            P = int(input[ptr])
            I = int(input[ptr+1])
            ptr += 2
            insort(buckets[I], P)
        else:
            ptr += 1
            A = int(input[ptr])
            B = int(input[ptr+1])
            ptr += 2
            min_val = float('inf')
            max_val = -float('inf')
            for i in range(A, B+1):
                if not buckets[i]:
                    continue
                current_min = buckets[i][0]
                current_max = buckets[i][-1]
                if current_min < min_val:
                    min_val = current_min
                if current_max > max_val:
                    max_val = current_max
            output.append(str(max_val - min_val))

    print('\n'.join(output))

if __name__ == '__main__':
    main()
