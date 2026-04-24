import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    heights = list(map(int, data[1:1+n]))

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], heights[i])

    right_max[n-1] = heights[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i])

    covered = 0
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        if water_level - heights[i] >= 1:
            covered += 1

    print(covered)

if __name__ == "__main__":
    main()