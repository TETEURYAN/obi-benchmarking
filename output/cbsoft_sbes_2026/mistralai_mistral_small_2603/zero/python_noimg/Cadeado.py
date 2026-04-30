
def min_clicks(N, disks):
    total = 0
    for c, s in disks:
        diff = abs(c - s)
        total += min(diff, 10 - diff)
    return total

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    disks = []
    for _ in range(N):
        c = int(input[ptr])
        s = int(input[ptr + 1])
        disks.append((c, s))
        ptr += 2
    print(min_clicks(N, disks))

if __name__ == "__main__":
    main()
