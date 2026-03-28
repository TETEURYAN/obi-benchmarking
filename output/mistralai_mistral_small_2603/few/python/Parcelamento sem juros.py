
import sys

def main():
    data = sys.stdin.read().split()
    V = int(data[0])
    P = int(data[1])
    base = V // P
    remainder = V % P
    for i in range(P):
        if i < remainder:
            print(base + 1)
        else:
            print(base)

if __name__ == "__main__":
    main()
