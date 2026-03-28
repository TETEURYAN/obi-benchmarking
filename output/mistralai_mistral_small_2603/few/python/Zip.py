import sys

def calculate_score(card1, card2):
    if card1 == card2:
        return 2 * (card1 + card2)
    elif abs(card1 - card2) == 1:
        return 3 * (card1 + card2)
    else:
        return card1 + card2

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    lia1 = int(data[0])
    lia2 = int(data[1])
    carolina1 = int(data[2])
    carolina2 = int(data[3])

    score_lia = calculate_score(lia1, lia2)
    score_carolina = calculate_score(carolina1, carolina2)

    if score_lia > score_carolina:
        print("Lia")
    elif score_carolina > score_lia:
        print("Carolina")
    else:
        print("empate")

if __name__ == "__main__":
    main()