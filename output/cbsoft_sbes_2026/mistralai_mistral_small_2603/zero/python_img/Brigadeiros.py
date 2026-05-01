
def main():
    import sys
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr]); ptr += 1
    K = int(data[ptr]); ptr += 1
    T = int(data[ptr]); ptr += 1
    P = list(map(int, data[ptr:ptr+N])); ptr += N
    G = list(map(int, data[ptr:ptr+N])); ptr += N

    positions = [i for i in range(N) if G[i] == 1]

    if T == 0:
        total = 0
        for pos in positions:
            total += P[pos]
        print(total)
        return

    positions.sort()
    best = 0
    for i in range(N):
        current = 0
        count = 0
        left = i
        right = i
        for pos in positions:
            if pos < left:
                cost = left - pos
                if cost > T:
                    break
                current += P[pos]
                count += 1
            elif pos > right:
                cost = pos - right
                if cost > T:
                    break
                current += P[pos]
                count += 1
            else:
                current += P[pos]
                count += 1
        if count == K:
            best = max(best, current)

    if best != 0:
        print(best)
        return

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            current = 0
            count = 0
            left = min(i, j)
            right = max(i, j)
            for pos in positions:
                if pos < left:
                    cost = left - pos
                    if cost > T:
                        break
                    current += P[pos]
                    count += 1
                elif pos > right:
                    cost = pos - right
                    if cost > T:
                        break
                    current += P[pos]
                    count += 1
                else:
                    current += P[pos]
                    count += 1
            if count == K:
                best = max(best, current)

    print(best)

if __name__ == '__main__':
    main()
