import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    nums = list(map(int, data[:4]))
    nums.sort()
    a, b, c, d = nums
    diff1 = abs((a + b) - (c + d))
    diff2 = abs((a + c) - (b + d))
    diff3 = abs((a + d) - (b + c))
    print(min(diff1, diff2, diff3))

if __name__ == "__main__":
    main()