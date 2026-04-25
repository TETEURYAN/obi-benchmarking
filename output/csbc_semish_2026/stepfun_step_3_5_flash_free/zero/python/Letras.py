
import sys
import bisect

def main():
    s = sys.stdin.readline().strip()
    tails = []
    for c in s:
        pos = bisect.bisect_right(tails, c)
        if pos == len(tails):
            tails.append(c)
        else:
            tails[pos] = c
    print(len(tails))

if __name__ == "__main__":
    main()
