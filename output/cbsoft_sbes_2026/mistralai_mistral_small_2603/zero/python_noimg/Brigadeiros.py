
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr]); ptr += 1
    K = int(data[ptr]); ptr += 1
    T = int(data[ptr]); ptr += 1

    P = list(map(int, data[ptr:ptr+N])); ptr += N
    G = list(map(int, data[ptr:ptr+N])); ptr += N

    positions = []
    for i in range(N):
        if G[i] == 1:
            positions.append(i)

    positions.sort()
    P_with_indices = [(P[i], i) for i in range(N)]
    P_with_indices.sort(reverse=True, key=lambda x: x[0])

    total = 0
    for i in range(K):
        total += P[positions[i]]

    if T == 0:
        print(total)
        return

    max_total = total
    for i in range(K):
        pos = positions[i]
        best = pos
        max_val = P[pos]
        for j in range(N):
            if P_with_indices[j][0] <= max_val:
                break
            target = P_with_indices[j][1]
            if target < pos:
                dist = pos - target
            else:
                dist = target - pos
            if dist <= T:
                if P_with_indices[j][0] > max_val:
                    max_val = P_with_indices[j][0]
                    best = target
        total = total - P[positions[i]] + max_val
        if total > max_total:
            max_total = total

    print(max_total)

if __name__ == "__main__":
    main()
