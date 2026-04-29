import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    children = [[] for _ in range(n + 1)]
    root = -1

    for _ in range(n):
        i, j = map(int, input().split())
        if j == 0:
            root = i
        else:
            children[j].append(i)

    size = [0] * (n + 1)
    balanced = True

    stack = [(root, 0)]
    while stack:
        node, state = stack.pop()
        if state == 0:
            stack.append((node, 1))
            for child in children[node]:
                stack.append((child, 0))
        else:
            total = 1
            if children[node]:
                expected = size[children[node][0]]
                for child in children[node]:
                    if size[child] != expected:
                        balanced = False
                    total += size[child]
            size[node] = total

    print("bem" if balanced else "mal")

if __name__ == "__main__":
    main()