
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    fita = list(map(int, input[ptr:ptr+N]))
    ptr += N

    zeros = [i for i, x in enumerate(fita) if x == 0]

    for i in range(N):
        if fita[i] == -1:
            min_dist = float('inf')
            for z in zeros:
                dist = abs(i - z)
                if dist < min_dist:
                    min_dist = dist
            fita[i] = min_dist if min_dist < 9 else 9

    print(' '.join(map(str, fita)))

if __name__ == "__main__":
    main()
