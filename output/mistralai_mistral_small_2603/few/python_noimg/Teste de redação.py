import sys
import random

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    M = int(data[1])

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    words = []
    distinct_words = set()

    # Generate M/2 distinct words first to ensure minimum distinct words
    for _ in range(M // 2):
        word = ''.join(random.choices(alphabet, k=random.randint(1, 10)))
        words.append(word)
        distinct_words.add(word)

    # Fill the remaining words (up to M) with any words (can repeat)
    remaining = M - len(words)
    for _ in range(remaining):
        word = ''.join(random.choices(alphabet, k=random.randint(1, 10)))
        words.append(word)

    # Ensure at least N words
    if len(words) < N:
        additional = N - len(words)
        for _ in range(additional):
            word = ''.join(random.choices(alphabet, k=random.randint(1, 10)))
            words.append(word)

    # Shuffle to make it random
    random.shuffle(words)

    # Ensure at least N words and at least M/2 distinct words
    # (The above steps should already guarantee this, but just to be safe)
    distinct_count = len(set(words))
    if distinct_count < M // 2:
        # If not enough distinct words, add more distinct ones
        needed = (M // 2) - distinct_count
        for _ in range(needed):
            word = ''.join(random.choices(alphabet, k=random.randint(1, 10)))
            words.append(word)
            distinct_words.add(word)

    # Ensure the total words is between N and M
    if len(words) > M:
        words = words[:M]
    elif len(words) < N:
        additional = N - len(words)
        for _ in range(additional):
            word = ''.join(random.choices(alphabet, k=random.randint(1, 10)))
            words.append(word)

    # Shuffle again to ensure randomness
    random.shuffle(words)

    print(' '.join(words))

if __name__ == "__main__":
    main()