import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    notas = list(map(int, data[1:1 + n]))

    freq = [0] * 101
    for nota in notas:
        freq[nota] += 1

    max_freq = -1
    best_nota = -1
    for nota in range(101):
        if freq[nota] > max_freq:
            max_freq = freq[nota]
            best_nota = nota
        elif freq[nota] == max_freq and nota > best_nota:
            best_nota = nota

    print(best_nota)

if __name__ == "__main__":
    solve()