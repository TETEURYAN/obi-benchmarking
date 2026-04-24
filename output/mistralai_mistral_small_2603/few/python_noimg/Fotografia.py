
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return

    A = int(data[0])
    L = int(data[1])
    N = int(data[2])
    frames = []
    idx = 3
    for i in range(N):
        X = int(data[idx])
        Y = int(data[idx+1])
        idx += 2
        frames.append((X, Y, i+1))

    min_area_diff = float('inf')
    best_id = -1

    for X, Y, id in frames:
        if (X >= A and Y >= L) or (X >= L and Y >= A):
            if X >= A and Y >= L:
                area_diff = X * Y - A * L
            else:
                area_diff = X * Y - A * L
            if area_diff < min_area_diff:
                min_area_diff = area_diff
                best_id = id
            elif area_diff == min_area_diff and id < best_id:
                best_id = id

    print(best_id)

if __name__ == "__main__":
    main()
