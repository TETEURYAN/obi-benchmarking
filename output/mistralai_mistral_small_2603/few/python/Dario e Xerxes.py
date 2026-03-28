
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    dario_wins = 0
    xerxes_wins = 0
    idx = 1
    for _ in range(n):
        d = int(data[idx])
        x = int(data[idx + 1])
        idx += 2
        if (x - d) % 5 in {1, 2}:
            xerxes_wins += 1
        else:
            dario_wins += 1
    print('dario' if dario_wins > xerxes_wins else 'xerxes')

if __name__ == '__main__':
    main()
