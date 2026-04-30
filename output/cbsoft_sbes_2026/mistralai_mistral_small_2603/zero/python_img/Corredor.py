
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    values = list(map(int, data[1:n+1]))

    max_sum = current_sum = 0
    for num in values:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum

    print(max_sum)

if __name__ == "__main__":
    main()
