import sys

def main():
    data = sys.stdin.readline().split()
    if not data:
        return
    n, s = map(int, data)

    if n == 1:
        print(s)
        return

    # Construct a matrix of the form a[i][j] = r[i] + c[j].
    # Then any legal choice (one per row and column) has constant sum:
    # sum_i r[i] + sum_j c[j].
    #
    # To ensure all entries are distinct, choose strictly increasing r and c
    # with gaps large enough so that all pairwise sums are unique.
    #
    # Let c[j] = j and r[i] = i * n.
    # Then a[i][j] = i*n + j are all distinct.
    #
    # Their legal-choice sum is:
    # R + C = n^2(n-1)/2 + n(n-1)/2 = (n-1)n(n+1)/2.
    # We shift only r[0] by delta so the total becomes s.
    # Distinctness is preserved because delta is chosen huge enough modulo range.
    #
    # More robustly, use a larger base B = 2n+1:
    # c[j] = j, r[i] = i*B.
    # Then all sums are unique since differences between rows are multiples of B
    # and column differences are in [-(n-1), n-1].
    B = 2 * n + 1

    base_sum = B * n * (n - 1) // 2 + n * (n - 1) // 2
    delta = s - base_sum

    out = []
    for i in range(n):
        ri = i * B + (delta if i == 0 else 0)
        row = [str(ri + j) for j in range(n)]
        out.append(" ".join(row))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
