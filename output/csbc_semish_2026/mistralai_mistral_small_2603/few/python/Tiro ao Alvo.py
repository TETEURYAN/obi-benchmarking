
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    C = int(data[idx])
    T = int(data[idx + 1])
    idx += 2

    radii = []
    for _ in range(C):
        radii.append(int(data[idx]))
        idx += 1

    total = 0
    for _ in range(T):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        dist_sq = x * x + y * y
        count = bisect.bisect_right(radii, dist_sq)
        total += count

    print(total)

if __name__ == "__main__":
    main()
