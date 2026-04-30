
def min_clicks(c, s):
    diff = abs(c - s)
    return min(diff, 10 - diff)

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    total = 0
    for _ in range(N):
        ci = int(input[ptr])
        si = int(input[ptr + 1])
        ptr += 2
        total += min_clicks(ci, si)
    print(total)

if __name__ == "__main__":
    main()
