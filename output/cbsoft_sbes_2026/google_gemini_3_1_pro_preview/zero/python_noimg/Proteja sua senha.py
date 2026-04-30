
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
            
        possible_passwords = [set("0123456789") for _ in range(6)]
        
        for _ in range(n):
            mapping = {}
            for i in range(5):
                d1 = next(iterator)
                d2 = next(iterator)
                mapping[chr(ord('A') + i)] = {d1, d2}
            
            for i in range(6):
                letter = next(iterator)
                possible_passwords[i] &= mapping[letter]
                
        print(f"Teste {test_case}")
        ans = [list(possible_passwords[i])[0] for i in range(6)]
        for x in ans:
            sys.stdout.write(x + " ")
        sys.stdout.write("\n\n")
        
        test_case += 1

if __name__ == '__main__':
    main()
