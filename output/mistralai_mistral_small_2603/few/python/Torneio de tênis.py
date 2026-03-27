
import sys

def main():
    results = sys.stdin.read().splitlines()
    wins = sum(1 for res in results if res.strip() == 'V')
    if wins >= 5:
        print(1)
    elif wins >= 3:
        print(2)
    elif wins >= 1:
        print(3)
    else:
        print(-1)

if __name__ == "__main__":
    main()
