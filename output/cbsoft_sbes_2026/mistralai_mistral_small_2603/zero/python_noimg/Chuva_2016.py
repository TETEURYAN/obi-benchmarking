
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    heights = list(map(int, data[1:n+1]))

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
        water_level = min(left_max[i], right_max[i])
        if water_level > heights[i]:
            water += 1

    print(water)

if __name__ == "__main__":
    main()
