
import sys

def main():
    n = int(sys.stdin.readline())
    heights = [int(sys.stdin.readline()) for _ in range(n)]

    if n == 0:
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

    water_sections = 0
    for i in range(n):
        min_height = min(left_max[i], right_max[i])
        if min_height > heights[i]:
            water_sections += 1

    print(water_sections)

if __name__ == "__main__":
    main()
