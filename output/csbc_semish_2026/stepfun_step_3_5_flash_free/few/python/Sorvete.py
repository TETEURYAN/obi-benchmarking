import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    test_num = 1
    outputs = []
    while idx < len(data):
        P = int(data[idx]); S = int(data[idx+1]); idx += 2
        if P == 0 and S == 0:
            break
        intervals = []
        for _ in range(S):
            u = int(data[idx]); v = int(data[idx+1]); idx += 2
            intervals.append((u, v))
        intervals.sort(key=lambda x: x[0])
        merged = []
        for u, v in intervals:
            if not merged:
                merged.append([u, v])
            else:
                if u <= merged[-1][1]:
                    merged[-1][1] = max(merged[-1][1], v)
                else:
                    merged.append([u, v])
        lines = [f"Teste {test_num}"]
        for u, v in merged:
            lines.append(f"{u} {v}")
        outputs.append("\n".join(lines))
        test_num += 1
    print("\n\n".join(outputs))

if __name__ == "__main__":
    main()