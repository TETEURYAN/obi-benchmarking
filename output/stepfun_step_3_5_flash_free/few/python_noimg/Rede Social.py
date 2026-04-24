import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    R = list(map(int, data[1:1+n]))
    R.sort(reverse=True)
    ans = 0
    for k in range(1, n+1):
        if R[k-1] >= k:
            ans = k
        else:
            break
    print(ans)

if __name__ == "__main__":
    main()