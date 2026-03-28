import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    heights = list(map(int, data[1:n+1]))

    has_multiple_peaks = False
    for i in range(1, n-1):
        if heights[i-1] > heights[i] and heights[i] < heights[i+1]:
            has_multiple_peaks = True
            break

    print('S' if has_multiple_peaks else 'N')

if __name__ == "__main__":
    main()