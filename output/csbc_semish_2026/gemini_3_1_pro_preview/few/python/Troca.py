import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    T = int(input_data[1])

    up = input_data[2 : 2+N]
    down = input_data[2+N : 2+2*N]

    flips = [0] * (N + 2)

    idx = 2 + 2*N
    for _ in range(T):
        I = int(input_data[idx])
        J = int(input_data[idx+1])
        flips[I] += 1
        flips[J+1] -= 1
        idx += 2

    ans = []
    current_flips = 0
    for i in range(1, N + 1):
        current_flips += flips[i]
        if current_flips % 2 != 0:
            ans.append(down[i-1])
        else:
            ans.append(up[i-1])

    sys.stdout.write(" ".join(ans) + "\n")

if __name__ == '__main__':
    main()