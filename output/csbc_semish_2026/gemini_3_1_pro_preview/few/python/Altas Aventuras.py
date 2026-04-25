import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    
    k = min(k, 30)
    
    def check(t):
        total = 0
        term = 1
        for i in range(1, k + 1):
            term = term * (t - i + 1) // i
            total += term
            if total >= n:
                return True
        return False

    low = 1
    high = n
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == '__main__':
    solve()