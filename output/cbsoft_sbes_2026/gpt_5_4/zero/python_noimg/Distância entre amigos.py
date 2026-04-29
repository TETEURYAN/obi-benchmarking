import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1+n]

    pref = [0] * n
    pref[0] = a[0] - 0
    for i in range(1, n):
        v = a[i] - i
        pref[i] = pref[i - 1] if pref[i - 1] > v else v

    ans = 0
    for j in range(1, n):
        cand = a[j] + j + pref[j - 1]
        if cand > ans:
            ans = cand

    print(ans)

if __name__ == "__main__":
    main()
