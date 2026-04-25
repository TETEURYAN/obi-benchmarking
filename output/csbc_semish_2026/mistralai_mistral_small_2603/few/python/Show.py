
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return

    A = int(data[0])
    N = int(data[1])
    M = int(data[2])

    rows = []
    idx = 3
    for _ in range(N):
        row = list(map(int, data[idx:idx+M]))
        rows.append(row)
        idx += M

    for i in range(N-1, -1, -1):
        row = rows[i]
        start = 0
        while start <= M - A:
            if all(x == 0 for x in row[start:start+A]):
                print(N - i)
                return
            start += 1

    print(-1)

if __name__ == "__main__":
    main()
