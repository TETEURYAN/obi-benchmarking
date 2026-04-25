import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    passwords = input_data[1:n+1]
    
    counts = {}
    for p in passwords:
        counts[p] = counts.get(p, 0) + 1
        
    ans = 0
    
    for p, cnt_p in counts.items():
        subs = set()
        len_p = len(p)
        for i in range(len_p):
            for j in range(i + 1, len_p + 1):
                subs.add(p[i:j])
        
        for s in subs:
            if s in counts:
                cnt_s = counts[s]
                if s == p:
                    ans += cnt_p * (cnt_p - 1)
                else:
                    ans += cnt_p * cnt_s
                    
    print(ans)

if __name__ == '__main__':
    solve()