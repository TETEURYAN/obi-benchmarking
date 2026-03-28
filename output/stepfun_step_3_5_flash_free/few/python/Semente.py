import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    F = int(data[0])
    R = int(data[1])
    pos = list(map(int, data[2:2+R]))
    d1 = pos[0] - 1
    d2 = F - pos[-1]
    d3 = 0
    for i in range(R - 1):
        gap = pos[i+1] - pos[i]
        d_needed = gap // 2
        if d_needed > d3:
            d3 = d_needed
    d = max(d1, d2, d3)
    print(d)

if __name__ == "__main__":
    main()