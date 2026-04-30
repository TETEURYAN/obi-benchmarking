
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    heights = list(map(int, data[1:n+1]))

    count = 0
    max_so_far = 0
    for h in reversed(heights):
        if h >= max_so_far:
            max_so_far = h
        else:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
