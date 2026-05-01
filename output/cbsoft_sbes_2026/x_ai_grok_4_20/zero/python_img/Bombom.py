
import sys

input = sys.stdin.read
data = input().strip().split()

dominant_suit = data[0][1]

values = {
    'A': 10,
    'J': 11,
    'Q': 12,
    'K': 13
}

def get_value(card):
    figure = card[0]
    suit = card[1]
    val = values[figure]
    if suit == dominant_suit:
        val += 4
    return val

luana_cards = data[1:4]
edu_cards = data[4:7]

luana_score = sum(get_value(card) for card in luana_cards)
edu_score = sum(get_value(card) for card in edu_cards)

if luana_score > edu_score:
    print("Luana")
elif edu_score > luana_score:
    print("Edu")
else:
    print("empate")
