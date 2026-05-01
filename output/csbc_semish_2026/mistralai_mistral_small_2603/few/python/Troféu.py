
import sys

def main():
    scores = [int(sys.stdin.readline()) for _ in range(5)]
    max_score = scores[0]
    second_max = None

    for score in scores[1:]:
        if score < max_score:
            second_max = score
            break

    if second_max is None:
        print(f"{5} {0}")
        return

    count_trophies = scores.count(max_score)
    count_plaques = 0

    for score in scores:
        if score == second_max:
            count_plaques += 1

    print(f"{count_trophies} {count_plaques}")

if __name__ == "__main__":
    main()
