
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    numbers = list(map(int, data[2:2+n]))
    positions = list(map(int, data[2+n:2+n+m]))

    count = [0] * 10
    prev_pos = 1
    for pos in positions:
        start = min(prev_pos, pos)
        end = max(prev_pos, pos)
        for i in range(start, end + 1):
            num = numbers[i - 1]
            count[num] += 1
        prev_pos = pos

    print(' '.join(map(str, count)))

if __name__ == "__main__":
    main()
