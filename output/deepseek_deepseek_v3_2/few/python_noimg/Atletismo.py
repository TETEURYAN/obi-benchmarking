import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    ranking = [0] * (n + 1)
    for i in range(1, n + 1):
        athlete = int(data[i])
        ranking[athlete] = i
    for i in range(1, n + 1):
        print(ranking[i])

if __name__ == "__main__":
    main()