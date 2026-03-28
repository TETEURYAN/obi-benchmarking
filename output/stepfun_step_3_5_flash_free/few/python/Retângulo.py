import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    L = list(map(int, data[1:1+n]))
    total = sum(L)
    if total % 2 != 0:
        print('N')
        return
    half = total // 2
    pos = [0] * n
    for i in range(1, n):
        pos[i] = pos[i-1] + L[i-1]
    pos_set = set(pos)
    count = 0
    for p in pos_set:
        q = (p + half) % total
        if q in pos_set:
            count += 1
    print('S' if count >= 4 else 'N')

if __name__ == "__main__":
    main()