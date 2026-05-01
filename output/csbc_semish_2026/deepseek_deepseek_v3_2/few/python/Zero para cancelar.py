import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    stack = []
    total = 0
    idx = 1
    for _ in range(n):
        x = int(data[idx])
        idx += 1
        if x == 0:
            if stack:
                total -= stack.pop()
        else:
            stack.append(x)
            total += x
    print(total)

if __name__ == "__main__":
    main()