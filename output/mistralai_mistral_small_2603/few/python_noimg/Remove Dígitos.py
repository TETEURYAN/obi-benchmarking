
import sys

def min_rounds(n):
    rounds = 0
    while n > 0:
        digits = [int(d) for d in str(n)]
        max_digit = max(digits)
        n -= max_digit
        rounds += 1
    return rounds

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    print(min_rounds(n))

if __name__ == "__main__":
    main()
