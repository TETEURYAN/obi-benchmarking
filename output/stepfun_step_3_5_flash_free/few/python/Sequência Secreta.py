import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    seq = list(map(int, data[1:1+n]))
    
    dp1, dp2 = 0, 0
    for v in seq:
        if v == 1:
            new_dp1 = max(dp1, 1 + dp2)
            new_dp2 = dp2
        else:
            new_dp1 = dp1
            new_dp2 = max(dp2, 1 + dp1)
        dp1, dp2 = new_dp1, new_dp2
    
    print(max(dp1, dp2))

if __name__ == "__main__":
    main()