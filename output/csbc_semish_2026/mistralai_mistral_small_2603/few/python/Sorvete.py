
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    teste = 1
    while ptr < len(data):
        P = int(data[ptr])
        S = int(data[ptr+1])
        ptr += 2
        if P == 0 and S == 0:
            break
        intervals = []
        for _ in range(S):
            U = int(data[ptr])
            V = int(data[ptr+1])
            ptr += 2
            intervals.append((U, V))
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged:
                merged.append(list(interval))
            else:
                last = merged[-1]
                if interval[0] <= last[1]:
                    last[1] = max(last[1], interval[1])
                else:
                    merged.append(list(interval))
        print(f"Teste {teste}")
        for interval in merged:
            print(f"{interval[0]} {interval[1]}")
        print()
        teste += 1

if __name__ == "__main__":
    main()
