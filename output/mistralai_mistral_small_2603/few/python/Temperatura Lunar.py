
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    test_num = 1
    output_lines = []
    while ptr < len(data):
        N = int(data[ptr])
        M = int(data[ptr + 1])
        ptr += 2
        if N == 0 and M == 0:
            break
        temperatures = []
        for _ in range(N):
            temperatures.append(int(data[ptr]))
            ptr += 1
        min_avg = float('inf')
        max_avg = -float('inf')
        current_sum = sum(temperatures[:M])
        min_avg = current_sum
        max_avg = current_sum
        for i in range(M, N):
            current_sum += temperatures[i] - temperatures[i - M]
            if current_sum < min_avg:
                min_avg = current_sum
            if current_sum > max_avg:
                max_avg = current_sum
        min_avg = min_avg // M
        max_avg = max_avg // M
        output_lines.append(f"Teste {test_num}")
        output_lines.append(f"{min_avg} {max_avg}")
        output_lines.append("")
        test_num += 1
    print('\n'.join(output_lines))

if __name__ == "__main__":
    main()
