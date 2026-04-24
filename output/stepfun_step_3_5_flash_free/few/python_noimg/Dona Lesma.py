import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    A = int(data[0])
    S = int(data[1])
    D = int(data[2])
    if A <= S:
        print(1)
    else:
        diff = S - D
        dias = (A - S + diff - 1) // diff + 1
        print(dias)

if __name__ == "__main__":
    main()