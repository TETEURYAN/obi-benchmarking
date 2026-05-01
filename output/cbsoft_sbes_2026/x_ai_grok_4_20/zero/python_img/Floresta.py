
import sys
import math

def main():
    n = int(sys.stdin.readline().strip())
    if n % 3 != 0:
        print(0)
        return
    t = n // 3
    cnt = 0
    max_a = int(math.sqrt(t))
    for a in range(1, max_a + 1):
        if t % a == 0:
            b = t // a
            if a <= b:
                cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()
