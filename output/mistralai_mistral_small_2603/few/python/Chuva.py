
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    n = int(data[0])
    heights = list(map(int, data[1:n+1]))

    if n <= 2:
        print(0)
        return

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], heights[i])

    right_max[-1] = heights[-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i])

    water = 0
    for i in range(n):
        min_height = min(left_max[i], right_max[i])
        if min_height > heights[i]:
            water += min_height - heights[i]

    print(water)

if __name__ == "__main__":
    main()
