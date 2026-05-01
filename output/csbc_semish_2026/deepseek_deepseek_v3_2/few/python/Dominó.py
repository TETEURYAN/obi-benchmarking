import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    result = ((N + 1) * (N + 2)) // 2
    print(result)

if __name__ == "__main__":
    main()