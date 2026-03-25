import sys

def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    test_num = 1
    
    while True:
        P = int(data[idx]); idx += 1
        S = int(data[idx]); idx += 1
        if P == 0 and S == 0:
            break
        
        intervals = []
        for _ in range(S):
            U = int(data[idx]); idx += 1
            V = int(data[idx]); idx += 1
            intervals.append((U, V))
        
        intervals.sort()
        merged = []
        if intervals:
            cur_start, cur_end = intervals[0]
            for start, end in intervals[1:]:
                if start <= cur_end:
                    cur_end = max(cur_end, end)
                else:
                    merged.append((cur_start, cur_end))
                    cur_start, cur_end = start, end
            merged.append((cur_start, cur_end))
        
        print(f"Teste {test_num}")
        for start, end in merged:
            print(f"{start} {end}")
        print()
        test_num += 1

if __name__ == "__main__":
    main()