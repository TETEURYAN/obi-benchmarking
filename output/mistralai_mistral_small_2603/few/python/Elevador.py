import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print('N')
        return

    n = int(data[0])
    weights = list(map(int, data[1:n+1]))

    weights.sort()

    left = 0
    right = n - 1
    possible = True

    while left <= right:
        if weights[right] - weights[left] > 8:
            possible = False
            break
        left += 1
        right -= 1

    print('S' if possible else 'N')

if __name__ == '__main__':
    main()