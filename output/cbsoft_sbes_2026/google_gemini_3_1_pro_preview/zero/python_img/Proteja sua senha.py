
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    test_case = 1
    
    while True:
        try:
            n_str = next(iterator)
        except StopIteration:
            break
        n = int(n_str)
        if n == 0:
            break
            
        possible_digits = [set(str(d) for d in range(10)) for _ in range(6)]
        
        for _ in range(n):
            mapping = {}
            for i in range(5):
                d1 = next(iterator)
                d2 = next(iterator)
                mapping[chr(ord('A') + i)] = {d1, d2}
            
            for i in range(6):
                letter = next(iterator)
                possible_digits[i].intersection_update(mapping[letter])
                
        print(f"Teste {test_case}")
        password = [list(s)[0] for s in possible_digits]
        print(" ".join(password) + " ")
        print()
        
        test_case += 1

if __name__ == '__main__':
    main()
