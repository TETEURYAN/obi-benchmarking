import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    total = 0
    for _ in range(n):
        c = int(next(it))
        s = int(next(it))
        diff = abs(c - s)
        total += min(diff, 10 - diff)
    print(total)

if __name__ == "__main__":
    main()