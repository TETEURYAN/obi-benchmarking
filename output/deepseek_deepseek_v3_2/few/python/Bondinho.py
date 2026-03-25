import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A = int(data[0])
    M = int(data[1])
    total = A + M
    if total <= 50:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()