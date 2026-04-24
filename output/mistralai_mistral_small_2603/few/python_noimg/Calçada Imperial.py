
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    sequence = list(map(int, data[1:n+1]))

    max_count = 0
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                continue
            count = 0
            last = None
            for num in sequence:
                if num == a or num == b:
                    if num != last:
                        count += 1
                        last = num
            if count > max_count:
                max_count = count
    print(max_count)

if __name__ == "__main__":
    main()
