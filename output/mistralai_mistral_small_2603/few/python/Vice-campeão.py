import sys

def main():
    A, B, C = map(int, sys.stdin.read().split())
    scores = [A, B, C]
    scores.sort()
    print(scores[1])

if __name__ == "__main__":
    main()