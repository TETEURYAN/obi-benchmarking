import sys

def solve():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token
                
    tokens = get_tokens()
    
    try:
        N = int(next(tokens))
        K = int(next(tokens))
        U = int(next(tokens))
    except StopIteration:
        return
        
    contains = [[] for _ in range(U + 1)]
    
    for i in range(1, N + 1):
        for _ in range(K):
            num = int(next(tokens))
            contains[num].append(i)
            
    remaining = [K] * (N + 1)
    
    winners = []
    for _ in range(U):
        draw = int(next(tokens))
        
        for card in contains[draw]:
            remaining[card] -= 1
            if remaining[card] == 0:
                winners.append(card)
                
        if winners:
            winners.sort()
            print(*(winners))
            return

if __name__ == '__main__':
    solve()