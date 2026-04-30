
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    S = int(input_data[1])

    if N == 1:
        print(S)
        return

    M = 5000
    R = []
    R_set = set()
    for i in range(1, N - 1):
        R.append(i)
        R_set.add(i)

    sum_R_N_minus_2 = sum(R)
    for r_n_minus_1 in range(1, M):
        if r_n_minus_1 in R_set:
            continue
        r_n = (S - sum_R_N_minus_2 - r_n_minus_1) % M
        if r_n not in R_set and r_n != r_n_minus_1:
            R.append(r_n_minus_1)
            R.append(r_n)
            R_set.add(r_n_minus_1)
            R_set.add(r_n)
            break

    S_R = sum(R)
    K = (S - S_R) // M

    c = []
    c_set = set()
    for j in range(1, N - 1):
        val = j - N // 2
        c.append(val)
        c_set.add(val)

    sum_c_N_minus_2 = sum(c)
    c_n_minus_1 = N
    while True:
        if c_n_minus_1 in c_set:
            c_n_minus_1 += 1
            continue
        c_n = K - sum_c_N_minus_2 - c_n_minus_1
        if c_n not in c_set and c_n != c_n_minus_1:
            c.append(c_n_minus_1)
            c.append(c_n)
            c_set.add(c_n_minus_1)
            c_set.add(c_n)
            break
        c_n_minus_1 += 1

    C = [x * M for x in c]

    for i in range(N):
        row = [R[i] + C[j] for j in range(N)]
        print(*(row))

if __name__ == '__main__':
    solve()
