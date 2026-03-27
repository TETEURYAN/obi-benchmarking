
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    reposts = list(map(int, data[1:n+1]))
    reposts.sort(reverse=True)
    max_influence = 0
    for i in range(n):
        if reposts[i] >= i + 1:
            max_influence = i + 1
        else:
            break
    print(max_influence)

if __name__ == "__main__":
    main()
