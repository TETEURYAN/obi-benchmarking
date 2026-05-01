from collections import deque

def solve():
    import sys
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    cards = list(map(int, input_data[1:n+1]))
    
    # compra is a deque where we pop from left (front)
    compra = deque(cards)
    descarte = deque()  # we append to right, when flipped becomes new compra (reversed)
    
    next_card = 1
    rounds = 1
    
    while True:
        if not compra:
            # end of round, flip descarte to compra
            # descarte has cards face down, flip means reverse order becomes face up
            # cards were placed face down in order, so bottom of descarte is first placed
            # flipping: the last card placed becomes the first to be drawn
            # Actually: cards go to descarte face down in order they were drawn
            # When flipped, the order reverses - last card placed is now on top
            compra = deque(reversed(descarte))
            descarte = deque()
            rounds += 1
        
        card = compra.popleft()
        
        if card == next_card:
            # place in morto
            next_card += 1
            if card == n:
                break
            # continue looking for next_card, don't add to descarte
            # but we need to keep checking if next cards in compra match
            # Actually after finding a card, we continue from compra
            # Check if next cards also match (they might be sequential)
            while compra and compra[0] == next_card:
                compra.popleft()
                next_card += 1
                if next_card - 1 == n:
                    break
            if next_card - 1 == n:
                break
        else:
            descarte.append(card)
    
    print(rounds)

solve()