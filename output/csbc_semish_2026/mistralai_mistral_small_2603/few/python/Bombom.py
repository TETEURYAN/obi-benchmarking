
import sys

def calculate_value(card, dominant_suit):
    figure, suit = card[0], card[1]
    base_value = {'A': 10, 'J': 11, 'Q': 12, 'K': 13}[figure]
    if suit == dominant_suit:
        return base_value + 4
    return base_value

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    dominant_suit = data[0][1]
    luana_cards = data[1:4]
    edu_cards = data[4:7]

    luana_sum = sum(calculate_value(card, dominant_suit) for card in luana_cards)
    edu_sum = sum(calculate_value(card, dominant_suit) for card in edu_cards)

    if luana_sum > edu_sum:
        print("Luana")
    elif edu_sum > luana_sum:
        print("Edu")
    else:
        print("empate")

if __name__ == "__main__":
    main()
