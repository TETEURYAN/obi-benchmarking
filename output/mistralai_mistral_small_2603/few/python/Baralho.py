
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    cards = data[0]
    suits = ['C', 'E', 'U', 'P']
    expected = set(f"{i:02d}{suit}" for suit in suits for i in range(1, 14))
    present = set()

    for i in range(0, len(cards), 3):
        card = cards[i:i+3]
        if len(card) != 3:
            continue
        if card in present:
            print("erro")
            return
        present.add(card)

    missing = {}
    for suit in suits:
        suit_cards = [card for card in present if card.endswith(suit)]
        if len(suit_cards) > 13:
            print("erro")
            return
        missing[suit] = 13 - len(suit_cards)

    for suit in suits:
        if missing[suit] == 0:
            print(0)
        else:
            print(missing[suit])

if __name__ == "__main__":
    main()
