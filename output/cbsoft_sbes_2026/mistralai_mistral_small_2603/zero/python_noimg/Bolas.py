
from collections import Counter

def main():
    bolas = list(map(int, input().split()))
    count = Counter(bolas)

    max_count = max(count.values())
    if max_count <= 4:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()
