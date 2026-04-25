
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    sequence = list(map(int, data[1:n+1]))

    max_count = 0
    current_count = 0
    prev = None

    for num in sequence:
        if num != prev:
            current_count += 1
            prev = num
        else:
            if current_count > max_count:
                max_count = current_count
            current_count = 1
            prev = num

    if current_count > max_count:
        max_count = current_count

    print(max_count)

if __name__ == "__main__":
    main()
