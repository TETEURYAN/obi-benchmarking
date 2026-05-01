
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    seen = set()
    duplicate = False
    for _ in range(N):
        x = int(input[ptr])
        y = int(input[ptr + 1])
        ptr += 2
        if (x, y) in seen:
            duplicate = True
        seen.add((x, y))
    print(1 if duplicate else 0)

if __name__ == "__main__":
    main()
