import sys

lines = sys.stdin.read().split()

dominant_suit = lines[0][1]

figura_val = {'A': 10, 'J': 11, 'Q': 12, 'K': 13}

def card_value(card, dominant):
    fig = card[0]
    suit = card[1]
    base = figura_val[fig]
    if suit == dominant:
        base += 4
    return base

luana = lines[1:4]
edu = lines[4:7]

luana_score = sum(card_value(c, dominant_suit) for c in luana)
edu_score = sum(card_value(c, dominant_suit) for c in edu)

if luana_score > edu_score:
    print("Luana")
elif edu_score > luana_score:
    print("Edu")
else:
    print("empate")