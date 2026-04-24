
import sys

def main():
    data = sys.stdin.read().split()
    positions = list(map(int, data))

    pos_kung = positions.index(1)
    pos_lu = positions.index(9)

    def get_round(pos):
        if pos < 2:
            return 1
        elif pos < 4:
            return 2
        elif pos < 8:
            return 3
        else:
            return 4

    round_kung = get_round(pos_kung)
    round_lu = get_round(pos_lu)

    if round_kung == round_lu:
        if round_kung == 1:
            print("oitavas")
        elif round_kung == 2:
            print("quartas")
        elif round_kung == 3:
            print("semifinal")
        else:
            print("final")
    else:
        print("oitavas")

if __name__ == "__main__":
    main()
