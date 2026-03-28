
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))

    last_occurrence = {}
    max_len = 0
    left = 0

    for right in range(n):
        current = arr[right]
        if current in last_occurrence and last_occurrence[current] >= left:
            left = last_occurrence[current] + 1
        last_occurrence[current] = right
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len

    print(max_len)

if __name__ == "__main__":
    main()
