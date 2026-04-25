
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    rectangles = []
    idx = 1
    for _ in range(n):
        x1 = int(data[idx])
        y1 = int(data[idx+1])
        x2 = int(data[idx+2])
        y2 = int(data[idx+3])
        idx += 4
        rectangles.append((x1, y1, x2, y2))

    rectangles.sort(key=lambda r: (r[0], r[1], r[2], r[3]))

    count = 0
    for i in range(n):
        x1, y1, x2, y2 = rectangles[i]
        inside = False
        for j in range(i):
            x1j, y1j, x2j, y2j = rectangles[j]
            if x1j <= x1 and y1j >= y1 and x2j >= x2 and y2j <= y2:
                inside = True
                break
        if not inside:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
