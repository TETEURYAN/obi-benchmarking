
import sys

def main():
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())

    ana_chair = (1 + A) % 3
    beatriz_chair = (1 + B) % 3

    if beatriz_chair == ana_chair:
        beatriz_chair = (beatriz_chair + 1) % 3

    carolina_chair = 3 - ana_chair - beatriz_chair
    print(carolina_chair)

if __name__ == "__main__":
    main()
