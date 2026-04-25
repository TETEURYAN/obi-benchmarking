import sys

def main():
    X, Y = map(int, sys.stdin.read().split())
    if 0 <= X <= 432 and 0 <= Y <= 468:
        print("dentro")
    else:
        print("fora")

if __name__ == "__main__":
    main()