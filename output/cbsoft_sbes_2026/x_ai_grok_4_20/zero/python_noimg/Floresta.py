
import sys
import math

def main():
    n = int(sys.stdin.readline().strip())
    if n % 3 != 0:
        print(0)
        return
    t = n // 3
    count = 0
    max_a = int(math.sqrt(t))
    for a in range(1, max_a + 1):
        if t % a == 0:
            b = t // a
            if a <= b:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
