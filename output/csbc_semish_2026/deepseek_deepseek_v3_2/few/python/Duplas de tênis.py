import sys

def main():
    data = sys.stdin.read().strip().split()
    if len(data) != 4:
        return
    a, b, c, d = map(int, data)
    
    # Como os valores já estão ordenados (0 ≤ A ≤ B ≤ C ≤ D ≤ 10⁴),
    # podemos considerar apenas as três combinações de duplas possíveis:
    # (a+b) e (c+d), (a+c) e (b+d), (a+d) e (b+c)
    diff1 = abs((a + b) - (c + d))
    diff2 = abs((a + c) - (b + d))
    diff3 = abs((a + d) - (b + c))
    
    print(min(diff1, diff2, diff3))

if __name__ == "__main__":
    main()