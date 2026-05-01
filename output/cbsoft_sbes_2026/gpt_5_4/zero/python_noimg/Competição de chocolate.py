import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, m = map(int, data)
    print("Carlos" if n % (m + 1) == 0 else "Paula")

if __name__ == "__main__":
    main()
