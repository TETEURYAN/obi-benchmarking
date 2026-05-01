import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    rooms = data[1:1+n]

    best = current = rooms[0]
    for x in rooms[1:]:
        current = max(x, current + x)
        if current > best:
            best = current

    print(best)

if __name__ == "__main__":
    main()
