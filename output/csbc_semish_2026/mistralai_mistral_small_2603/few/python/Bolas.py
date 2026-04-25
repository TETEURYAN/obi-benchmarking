import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        print('N')
        return

    balls = list(map(int, data))
    freq = [0] * 10
    for num in balls:
        freq[num] += 1

    max_freq = max(freq)
    if max_freq <= 4:
        print('S')
    else:
        print('N')

solve()