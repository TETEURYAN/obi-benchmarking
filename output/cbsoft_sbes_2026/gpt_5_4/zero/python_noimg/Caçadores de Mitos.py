import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    seen = set()
    idx = 1

    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        p = x * 501 + y
        if p in seen:
            print(1)
            return
        seen.add(p)

    print(0)

if __name__ == "__main__":
    main()
