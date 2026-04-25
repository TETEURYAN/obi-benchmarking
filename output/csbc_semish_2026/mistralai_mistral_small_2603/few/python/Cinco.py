
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    digits = list(map(int, data[1:n+1]))
    
    last_digit = digits[-1]
    if last_digit % 5 == 0:
        print(*digits)
        return
    
    candidates = []
    for i in range(n):
        if digits[i] % 5 == 0:
            candidates.append(i)
    
    if not candidates:
        print(-1)
        return
    
    max_num = -1
    best_swap = None
    original = digits.copy()
    
    for pos in candidates:
        for i in range(n-1, -1, -1):
            if i == pos:
                continue
            if digits[i] % 5 == 0:
                continue
            new_digits = digits.copy()
            new_digits[pos], new_digits[i] = new_digits[i], new_digits[pos]
            num = int(''.join(map(str, new_digits)))
            if num > max_num:
                max_num = num
                best_swap = new_digits
    
    if best_swap is None:
        print(-1)
    else:
        print(*best_swap)

if __name__ == "__main__":
    main()
