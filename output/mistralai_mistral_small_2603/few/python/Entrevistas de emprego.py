
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1

    adj = [set() for _ in range(N + 1)]
    for i in range(1, N + 1):
        line = data[ptr]
        ptr += 1
        for j in range(1, N + 1):
            if line[j - 1] == '1':
                adj[i].add(j)

    E = int(data[ptr])
    ptr += 1

    out_lines = []
    for _ in range(E):
        K = int(data[ptr])
        ptr += 1
        candidates = list(map(int, data[ptr:ptr + K]))
        ptr += K

        valid = True
        for i in range(K):
            for j in range(i + 1, K):
                u = candidates[i]
                v = candidates[j]
                if v in adj[u]:
                    valid = False
                    break
            if not valid:
                break

        out_lines.append('S' if not valid else 'N')

    print('\n'.join(out_lines))

if __name__ == '__main__':
    main()
