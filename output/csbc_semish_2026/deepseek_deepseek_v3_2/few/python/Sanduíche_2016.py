import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    D = int(next(it))
    C = [int(next(it)) for _ in range(N)]

    total_sum = sum(C)
    if total_sum < D:
        print(0)
        return

    # Caso 1: sequência contínua no meio
    ans = 0
    current_sum = 0
    left = 0
    for right in range(N):
        current_sum += C[right]
        while current_sum > D and left <= right:
            current_sum -= C[left]
            left += 1
        if current_sum == D:
            ans += 1

    # Caso 2: prefixo + sufixo (extremidades)
    # Para cada prefixo de comprimento i, queremos sufixo de comprimento j tal que:
    # prefix_sum[i] + suffix_sum[j] == D, com i + j < N (pois não pode pegar tudo)
    prefix_sums = [0] * (N + 1)
    for i in range(N):
        prefix_sums[i + 1] = prefix_sums[i] + C[i]

    suffix_sums = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        suffix_sums[i] = suffix_sums[i + 1] + C[i]

    # Para cada prefixo de comprimento i (0 <= i < N), queremos sufixo de comprimento j (1 <= j <= N - i - 1)
    # suffix_sums[N - j] é a soma dos últimos j elementos
    # Queremos prefix_sums[i] + suffix_sums[N - j] == D
    # suffix_sums[N - j] == D - prefix_sums[i]
    # Vamos contar quantos j satisfazem isso.

    # Pré‑computar frequências dos sufixos válidos
    from collections import defaultdict
    suffix_freq = defaultdict(int)
    # j é o comprimento do sufixo, j >= 1
    for j in range(1, N):
        suffix_val = suffix_sums[N - j]
        suffix_freq[suffix_val] += 1

    # Para cada prefixo i (0 <= i < N-1), porque i+j < N => j >= 1
    for i in range(N - 1):
        need = D - prefix_sums[i]
        if need in suffix_freq:
            ans += suffix_freq[need]
        # Remover o sufixo de comprimento (N - i - 1) da contagem futura
        # porque quando avançamos i, o sufixo de comprimento (N - i - 1) não será mais válido
        # (pois i+j < N => j <= N - i - 1)
        suffix_to_remove = suffix_sums[i + 1]
        suffix_freq[suffix_to_remove] -= 1
        if suffix_freq[suffix_to_remove] == 0:
            del suffix_freq[suffix_to_remove]

    print(ans)

if __name__ == "__main__":
    main()