
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    trees = []
    index = 1
    for i in range(n):
        x = int(data[index])
        h = int(data[index + 1])
        trees.append((x, h))
        index += 2

    trees.sort()
    stack = []
    for x, h in trees:
        while stack:
            prev_x, prev_h = stack[-1]
            if (h - (x - prev_x)) >= prev_h:
                stack.pop()
            else:
                break
        stack.append((x, h))

    print(len(stack) - 1)

if __name__ == "__main__":
    main()
