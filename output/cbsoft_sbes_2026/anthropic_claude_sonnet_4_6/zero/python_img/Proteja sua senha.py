import sys

def solve():
    input_data = sys.stdin.read().split('\n')
    idx = 0
    test_num = 0
    
    while idx < len(input_data):
        line = input_data[idx].strip()
        idx += 1
        if not line:
            continue
        N = int(line)
        if N == 0:
            break
        
        test_num += 1
        
        # For each digit 0-9, we'll track which letters it could be associated with
        # Each association line gives us: 10 digits (2 per letter A-E) and 6 letters
        # digit_to_letter[d] = set of possible letters
        # But we need to find the actual password digits
        
        # Let's think differently:
        # For each association, we know which letter maps to which pair of digits
        # The password letters tell us which pair each password digit belongs to
        # We need to find the unique digit for each position
        
        # For each password position, across all N associations,
        # the digit must be in the intersection of the pairs given by the letter for that position
        
        # password_candidates[pos] = set of possible digits
        password_candidates = [set(range(10)) for _ in range(6)]
        
        associations = []
        for _ in range(N):
            line = input_data[idx].strip()
            idx += 1
            parts = line.split()
            # 10 digits + 6 letters = 16 parts
            digits = parts[:10]
            letters = parts[10:16]
            
            # Build letter to digits mapping
            letter_to_digits = {}
            for i, letter in enumerate('ABCDE'):
                d1 = int(digits[2*i])
                d2 = int(digits[2*i+1])
                letter_to_digits[letter] = {d1, d2}
            
            # For each password position, intersect with the pair for that letter
            for pos in range(6):
                letter = letters[pos]
                possible = letter_to_digits[letter]
                password_candidates[pos] = password_candidates[pos] & possible
        
        # Now each position should have exactly one digit
        password = []
        for pos in range(6):
            # Should be unique
            digit = list(password_candidates[pos])[0]
            password.append(str(digit))
        
        print(f"Teste {test_num}")
        print(' '.join(password))
        print()

solve()