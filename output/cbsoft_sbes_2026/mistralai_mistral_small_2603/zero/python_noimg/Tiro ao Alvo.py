
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    C = int(data[ptr])
    ptr += 1
    T = int(data[ptr])
    ptr += 1

    radii = []
    for _ in range(C):
        radii.append(int(data[ptr]))
        ptr += 1

    total_points = 0
    for _ in range(T):
        x = int(data[ptr])
        y = int(data[ptr + 1])
        ptr += 2
        distance_sq = x * x + y * y
        points = 0
        for r in radii:
            if distance_sq <= r * r:
                points += 1
            else:
                break
        total_points += points

    print(total_points)

if __name__ == "__main__":
    main()
