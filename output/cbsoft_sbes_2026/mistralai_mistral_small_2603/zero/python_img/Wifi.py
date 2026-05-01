
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    rects = []
    index = 1
    for i in range(n):
        x1 = int(data[index])
        y1 = int(data[index+1])
        x2 = int(data[index+2])
        y2 = int(data[index+3])
        index += 4
        rects.append((x1, y1, x2, y2))

    rects.sort(key=lambda r: (r[0], r[1], r[2], r[3]))

    stack = []
    for rect in rects:
        x1, y1, x2, y2 = rect
        while stack:
            top = stack[-1]
            if top[0] <= x1 and top[1] <= y1 and top[2] >= x2 and top[3] >= y2:
                break
            stack.pop()
        stack.append(rect)

    print(len(stack))

if __name__ == "__main__":
    main()
