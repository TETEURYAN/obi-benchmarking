import sys

def solve():
    def get_ints():
        for line in sys.stdin:
            for token in line.split():
                yield int(token)
                
    tokens = get_ints()
    
    try:
        N = next(tokens)
        K = next(tokens)
        U = next(tokens)
    except StopIteration:
        return
        
    cards_with_number = [[] for _ in range(U + 1)]
    
    for i in range(1, N + 1):
        for _ in range(K):
            num = next(tokens)
            cards_with_number[num].append(i)
            
    remaining = [K] * (N + 1)
    winners = []
    
    for drawn in tokens:
        for card in cards_with_number[drawn]:
            remaining[card] -= 1
            if remaining[card] == 0:
                winners.append(card)
                
        if winners:
            winners.sort()
            print(*(winners))
            return

if __name__ == '__main__':
    solve()