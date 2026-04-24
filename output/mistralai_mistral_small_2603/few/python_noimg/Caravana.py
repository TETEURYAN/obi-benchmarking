import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    weights = list(map(int, data[1:1+n]))

    total = sum(weights)
    target = total // n

    for w in weights:
        print(w - target)

if __name__ == "__main__":
    main()