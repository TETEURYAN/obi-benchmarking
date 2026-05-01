import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    print((N + 1) * (N + 2) // 2)

if __name__ == "__main__":
    main()