import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    seen = bytearray(501 * 501)
    idx = 1

    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        pos = x * 501 + y
        if seen[pos]:
            print(1)
            return
        seen[pos] = 1

    print(0)

if __name__ == "__main__":
    main()
