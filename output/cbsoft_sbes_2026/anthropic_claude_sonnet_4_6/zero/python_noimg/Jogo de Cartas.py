from collections import deque

def solve():
    import sys
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    cards = list(map(int, input_data[1:n+1]))
    
    # compra is a deque where we pop from left (front)
    compra = deque(cards)
    descarte = deque()
    
    next_card = 1
    rounds = 1
    
    while next_card <= n:
        # Search through compra for next_card
        found = False
        while compra:
            card = compra.popleft()
            if card == next_card:
                next_card += 1
                found = True
                # Continue searching for next cards in same round pass
                # Actually we just continue the loop
                break
            else:
                descarte.append(card)
        
        if not found:
            # End of round, flip descarte to become compra
            # descarte was built by appending, so last appended is at right
            # We need to flip it: the bottom of descarte becomes top of compra
            # descarte cards are face down, when flipped they go face up
            # The order: first card put in descarte is at bottom, last at top
            # When flipped, first card put becomes top of new compra
            # So we reverse descarte to get compra
            compra = deque(reversed(descarte))
            descarte = deque()
            rounds += 1
    
    print(rounds)

solve()