
def main():
    n = int(input())
    dario_wins = 0
    xerxes_wins = 0
    for _ in range(n):
        d, x = map(int, input().split())
        if (d == 0 and (x == 1 or x == 2)) or (d == 1 and (x == 2 or x == 3)) or (d == 2 and (x == 3 or x == 4)) or (d == 3 and (x == 4 or x == 0)) or (d == 4 and (x == 0 or x == 1)):
            dario_wins += 1
        else:
            xerxes_wins += 1
    print('dario' if dario_wins > xerxes_wins else 'xerxes')

if __name__ == '__main__':
    main()
