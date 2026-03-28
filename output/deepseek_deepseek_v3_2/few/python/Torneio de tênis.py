import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    wins = data.count('V')
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