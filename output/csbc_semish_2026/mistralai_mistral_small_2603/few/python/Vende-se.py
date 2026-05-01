
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    positions = list(map(int, data[2:2+n]))
    positions.sort()
    min_distance = float('inf')
    for i in range(n - (n - k)):
        distance = positions[i + (n - k) - 1] - positions[i]
        if distance < min_distance:
            min_distance = distance
    print(min_distance)

if __name__ == "__main__":
    main()
