
import sys

def main():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    acc = 0
    days = 0
    target = 1000000
    
    for i in range(1, N + 1):
        acc += int(data[i])
        days += 1
        if acc >= target:
            print(days)
            return
    
    # A garantia é que a soma total >= target, então sempre imprimirá.

if __name__ == "__main__":
    main()
