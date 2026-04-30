cards = []
for _ in range(7):
    cards.append(input().strip())

dominant_suit = cards[0][1]

figura_value = {'A': 10, 'J': 11, 'Q': 12, 'K': 13}

def card_value(card, dominant):
    fig = card[0]
    suit = card[1]
    base = figura_value[fig]
    if suit == dominant:
        base += 4
    return base

luana_cards = cards[1:4]
edu_cards = cards[4:7]

luana_score = sum(card_value(c, dominant_suit) for c in luana_cards)
edu_score = sum(card_value(c, dominant_suit) for c in edu_cards)

if luana_score > edu_score:
    print("Luana")
elif edu_score > luana_score:
    print("Edu")
else:
    print("empate")