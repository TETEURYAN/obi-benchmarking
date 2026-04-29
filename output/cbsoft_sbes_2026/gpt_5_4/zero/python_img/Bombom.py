cards = [input().strip() for _ in range(7)]

dominant_suit = cards[0][1]

base_value = {
    'A': 10,
    'J': 11,
    'Q': 12,
    'K': 13
}

def value(card):
    fig, suit = card[0], card[1]
    v = base_value[fig]
    if suit == dominant_suit:
        v += 4
    return v

luana = sum(value(cards[i]) for i in range(1, 4))
edu = sum(value(cards[i]) for i in range(4, 7))

if luana > edu:
    print("Luana")
elif edu > luana:
    print("Edu")
else:
    print("empate")