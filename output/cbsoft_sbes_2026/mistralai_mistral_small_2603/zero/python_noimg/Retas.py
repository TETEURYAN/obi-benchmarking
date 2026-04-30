
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1
    X1 = int(data[ptr])
    ptr += 1
    X2 = int(data[ptr])
    ptr += 1

    lines = []
    for _ in range(N):
        A = int(data[ptr])
        ptr += 1
        B = int(data[ptr])
        ptr += 1
        lines.append((A, B))

    if N < 2:
        print(0)
        return

    events = []
    for i in range(N):
        A_i, B_i = lines[i]
        for j in range(i + 1, N):
            A_j, B_j = lines[j]
            if A_i == A_j:
                continue
            x_intersect = (B_j - B_i) / (A_i - A_j)
            if X1 <= x_intersect <= X2:
                events.append(x_intersect)

    print(len(events))

if __name__ == "__main__":
    main()
