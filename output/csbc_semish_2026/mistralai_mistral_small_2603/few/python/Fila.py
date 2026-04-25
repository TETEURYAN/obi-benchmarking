
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    queue = list(map(int, data[1:n+1]))
    m = int(data[n+1])
    left = list(map(int, data[n+2:n+2+m]))

    left_set = set(left)
    result = [str(x) for x in queue if x not in left_set]

    print(' '.join(result))

if __name__ == "__main__":
    main()
