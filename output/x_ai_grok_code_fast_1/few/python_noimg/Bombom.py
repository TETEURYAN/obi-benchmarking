import sys

input_data = sys.stdin.read().split()

dominant_suit = input_data[0][1]

def get_value(card):
    fig = card[0]
    base = {'A':10, 'J':11, 'Q':12, 'K':13}[fig]
    if card[1] == dominant_suit:
        base += 4
    return base

luana_cards = input_data[1:4]
edu_cards = input_data[4:7]

sum_luana = sum(get_value(c) for c in luana_cards)
sum_edu = sum(get_value(c) for c in edu_cards)

if sum_luana > sum_edu:
    print("Luana")
elif sum_edu > sum_luana:
    print("Edu")
else:
    print("empate")