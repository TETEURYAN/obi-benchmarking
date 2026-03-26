
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    seq = data[1:]
    count = 0
    for i in range(n - 2):
        if seq[i] == '1' and seq[i + 1] == '0' and seq[i + 2] == '0':
            count += 1
    print(count)

if __name__ == "__main__":
    main()
