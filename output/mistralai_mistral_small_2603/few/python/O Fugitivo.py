
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    n = int(data[0])
    m = int(data[1])
    max_dist_sq = m * m

    x = 0
    y = 0
    exceeded = False

    idx = 2
    for _ in range(n):
        direction = data[idx]
        distance = int(data[idx + 1])
        idx += 2

        if direction == 'N':
            y += distance
        elif direction == 'S':
            y -= distance
        elif direction == 'L':
            x += distance
        elif direction == 'O':
            x -= distance

        dist_sq = x * x + y * y
        if dist_sq > max_dist_sq:
            exceeded = True
            break

    print(1 if exceeded else 0)

if __name__ == "__main__":
    main()
