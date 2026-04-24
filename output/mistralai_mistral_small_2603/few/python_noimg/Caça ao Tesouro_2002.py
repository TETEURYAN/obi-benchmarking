
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    test_num = 1
    output_lines = []

    while ptr < len(data):
        X = int(data[ptr])
        Y = int(data[ptr+1])
        N = int(data[ptr+2])
        ptr += 3

        if X == 0 and Y == 0 and N == 0:
            break

        arc_values = []
        for _ in range(N):
            arc_values.append(int(data[ptr]))
            ptr += 1

        total_joao = X
        total_jose = Y
        total_arca = sum(arc_values)

        possible = False
        if (total_joao + total_jose + total_arca) % 2 == 0:
            target = (total_joao + total_jose + total_arca) // 2
            if total_joao <= target and total_jose <= target:
                remaining = target - total_joao
                if remaining >= 0:
                    dp = [False] * (remaining + 1)
                    dp[0] = True
                    for val in arc_values:
                        for j in range(remaining, val - 1, -1):
                            if dp[j - val]:
                                dp[j] = True
                    if dp[remaining]:
                        possible = True

        output_lines.append(f"Teste {test_num}")
        output_lines.append('S' if possible else 'N')
        output_lines.append('')
        test_num += 1

    print('\n'.join(output_lines))

if __name__ == "__main__":
    main()
