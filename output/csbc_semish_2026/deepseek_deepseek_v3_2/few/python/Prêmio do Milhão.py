import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    total = 0
    for i in range(1, n + 1):
        total += int(data[i])
        if total >= 1000000:
            print(i)
            return

if __name__ == "__main__":
    main()