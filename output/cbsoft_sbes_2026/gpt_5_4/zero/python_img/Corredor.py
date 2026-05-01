import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1+n]

    best = current = a[0]
    for x in a[1:]:
        current = max(x, current + x)
        if current > best:
            best = current

    print(best)

if __name__ == "__main__":
    main()
