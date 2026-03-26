import sys

def solve():
    word = sys.stdin.read().split()[0]
    
    alphabet = "abcdefghijklmnopqrstuvxz"
    vowels = set("aeiou")
    
    # Build list of consonants in order
    consonants = [c for c in alphabet if c not in vowels]
    
    result = []
    
    for ch in word:
        if ch in vowels:
            result.append(ch)
        else:
            # It's a consonant
            # 1. The consonant itself
            # 2. Nearest vowel
            # 3. Next consonant in alphabet order
            
            pos_in_alpha = alphabet.index(ch)
            
            # Find nearest vowel
            best_vowel = None
            best_dist = float('inf')
            for v in "aeiou":
                if v in alphabet:
                    vpos = alphabet.index(v)
                    dist = abs(vpos - pos_in_alpha)
                    if dist < best_dist or (dist == best_dist and (best_vowel is None or alphabet.index(v) < alphabet.index(best_vowel))):
                        best_dist = dist
                        best_vowel = v
            
            # Find next consonant
            cons_idx = consonants.index(ch)
            if cons_idx + 1 < len(consonants):
                next_cons = consonants[cons_idx + 1]
            else:
                next_cons = ch  # z case
            
            result.append(ch + best_vowel + next_cons)
    
    print(''.join(result))

solve()