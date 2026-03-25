import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

word = input_data[0]

alphabet = "abcdefghijklmnopqrstuvxz"
vowels = "aeiou"

res = []
for char in word:
    if char in vowels:
        res.append(char)
    else:
        res.append(char)
        
        min_dist = 100
        best_v = ''
        c_idx = alphabet.index(char)
        for v in vowels:
            v_idx = alphabet.index(v)
            dist = abs(c_idx - v_idx)
            if dist < min_dist:
                min_dist = dist
                best_v = v
        res.append(best_v)
        
        nxt_c = 'z'
        for i in range(c_idx + 1, len(alphabet)):
            if alphabet[i] not in vowels:
                nxt_c = alphabet[i]
                break
        res.append(nxt_c)

print("".join(res))