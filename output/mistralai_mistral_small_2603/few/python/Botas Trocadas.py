import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    boots = []
    idx = 1
    for _ in range(n):
        size = int(data[idx])
        foot = data[idx + 1]
        boots.append((size, foot))
        idx += 2

    left = {}
    right = {}

    for size, foot in boots:
        if foot == 'E':
            if size in left:
                left[size] += 1
            else:
                left[size] = 1
        else:
            if size in right:
                right[size] += 1
            else:
                right[size] = 1

    pairs = 0
    for size in left:
        if size in right:
            pairs += min(left[size], right[size])

    print(pairs)

if __name__ == "__main__":
    main()