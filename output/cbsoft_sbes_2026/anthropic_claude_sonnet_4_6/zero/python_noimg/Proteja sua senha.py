import sys

def solve():
    input_data = sys.stdin.read().split('\n')
    line_idx = 0
    test_num = 0
    
    while line_idx < len(input_data):
        line = input_data[line_idx].strip()
        line_idx += 1
        
        if not line:
            continue
        
        N = int(line)
        if N == 0:
            break
        
        test_num += 1
        
        # For each association, we have 10 digits and 6 letters
        # digits[0..1] -> A, digits[2..3] -> B, digits[4..5] -> C, digits[6..7] -> D, digits[8..9] -> E
        
        associations = []
        for _ in range(N):
            parts = input_data[line_idx].strip().split()
            line_idx += 1
            digits = parts[:10]
            letters = parts[10:16]
            associations.append((digits, letters))
        
        # We need to find the 6-digit password
        # For each position in the password (0..5), the letter typed gives us 2 possible digits
        # We need to find which digit is consistent across all N associations
        
        password = []
        for pos in range(6):
            # For each association, get the possible digits for this position
            possible_sets = []
            for digits, letters in associations:
                letter = letters[pos]
                letter_idx = ord(letter) - ord('A')
                d1 = digits[letter_idx * 2]
                d2 = digits[letter_idx * 2 + 1]
                possible_sets.append({d1, d2})
            
            # Find the intersection
            result = possible_sets[0]
            for s in possible_sets[1:]:
                result = result & s
            
            # Should be exactly one digit
            password.append(list(result)[0])
        
        print(f"Teste {test_num}")
        print(' '.join(password))
        print()

solve()