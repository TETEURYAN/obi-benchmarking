
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    B = int(data[1])
    sizes = list(map(int, data[2:2+n]))
    sizes.sort()
    i = 0
    j = n - 1
    pairs = 0
    while i < j:
        if sizes[i] + sizes[j] <= B:
            pairs += 1
            i += 1
            j -= 1
        else:
            j -= 1
    print(n - pairs)

if __name__ == "__main__":
    main()
