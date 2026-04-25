
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    T = int(data[0])
    N = int(data[1])
    cities = list(map(int, data[2:2+N]))
    cities.sort()

    min_neighborhood = float('inf')

    for i in range(1, N-1):
        left = cities[i-1]
        right = cities[i+1]
        current = cities[i]
        neighborhood = min(current - left, right - current)
        if neighborhood < min_neighborhood:
            min_neighborhood = neighborhood

    print("{0:.2f}".format(min_neighborhood))

if __name__ == "__main__":
    main()
