import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    A = int(data[0])
    B = int(data[1])
    C = 2 * A - B
    print(C)

if __name__ == "__main__":
    main()