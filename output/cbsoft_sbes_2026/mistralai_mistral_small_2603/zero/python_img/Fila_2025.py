
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    heights = list(map(int, data[1:n+1]))

    count = 0
    max_so_far = 0

    for i in range(n-1, -1, -1):
        if i == n-1:
            max_so_far = heights[i]
        else:
            if heights[i] > max_so_far:
                max_so_far = heights[i]
            else:
                count += 1

    print(count)

if __name__ == "__main__":
    main()
