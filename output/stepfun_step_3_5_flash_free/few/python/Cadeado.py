import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    total = 0
    idx = 1
    for _ in range(n):
        c = int(data[idx])
        s = int(data[idx + 1])
        idx += 2
        diff = abs(c - s)
        total += min(diff, 10 - diff)
    print(total)

if __name__ == "__main__":
    main()