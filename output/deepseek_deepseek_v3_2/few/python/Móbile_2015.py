import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A, B, C, D = map(int, data[:4])
    if A == B + C + D and B + C == D and B == C:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()