import sys

def main():
    balls = sys.stdin.read().split()
    if not balls:
        return
    for b in set(balls):
        if balls.count(b) > 4:
            print("N")
            return
    print("S")

if __name__ == '__main__':
    main()