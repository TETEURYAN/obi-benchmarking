import sys

def main():
    IA, IB, FA, FB = map(int, sys.stdin.read().split())
    if (IA, IB) == (FA, FB):
        print(0)
        return
    if (IA, IB) == (FA, 1 - FB):
        print(1)
        return
    if (IA, IB) == (1 - FA, 1 - FB):
        print(2)
        return
    if (IA, IB) == (1 - FA, FB):
        print(1)
        return
    print(2)

if __name__ == "__main__":
    main()