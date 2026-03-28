import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    result = (2**n + 1) ** 2
    print(result)

if __name__ == "__main__":
    main()