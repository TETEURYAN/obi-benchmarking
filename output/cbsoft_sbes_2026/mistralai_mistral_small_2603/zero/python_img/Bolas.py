
from collections import Counter

def main():
    bolas = list(map(int, input().split()))
    freq = Counter(bolas)
    max_freq = max(freq.values())
    if max_freq <= 4:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()
