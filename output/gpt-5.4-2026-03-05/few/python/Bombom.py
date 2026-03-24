import sys

cards = sys.stdin.read().split()
dominant = cards[0][1]

base = {'A': 10, 'J': 11, 'Q': 12, 'K': 13}

def value(card):
    v = base[card[0]]
    if card[1] == dominant:
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