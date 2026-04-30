
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    seq = list(map(int, data[1:n+1]))

    max_count = 0
    for i in range(n):
        for j in range(i, n):
            current = []
            for k in range(i, j+1):
                if not current or seq[k] != current[-1]:
                    current.append(seq[k])
            if len(current) >= 2:
                distinct = set(current)
                if len(distinct) <= 2:
                    if len(current) > max_count:
                        max_count = len(current)
            else:
                if len(current) > max_count:
                    max_count = len(current)
    print(max_count)

if __name__ == "__main__":
    main()
