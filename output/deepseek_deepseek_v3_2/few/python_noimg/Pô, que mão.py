import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    costs = list(map(int, data[1:4]))
    costs.sort()
    count = 0
    total = 0
    for c in costs:
        if total + c <= N:
            total += c
            count += 1
        else:
            break
    print(count)

if __name__ == "__main__":
    main()