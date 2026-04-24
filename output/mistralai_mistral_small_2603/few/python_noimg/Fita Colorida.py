
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))

    result = [-1] * n
    zeros = [i for i, x in enumerate(arr) if x == 0]

    for i in range(n):
        if arr[i] == 0:
            result[i] = 0
        else:
            min_dist = float('inf')
            for z in zeros:
                dist = abs(i - z)
                if dist < min_dist:
                    min_dist = dist
            result[i] = min_dist if min_dist < 9 else 9

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
