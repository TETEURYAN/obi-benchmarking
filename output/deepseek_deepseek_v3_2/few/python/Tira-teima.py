import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    X, Y = map(int, data)
    if 0 <= X <= 432 and 0 <= Y <= 468:
        print("dentro")
    else:
        print("fora")

if __name__ == "__main__":
    main()