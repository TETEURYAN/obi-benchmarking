import sys

s = sys.stdin.read().strip()

vowels = "aeiou"
alphabet = "abcdefghijklmnopqrstuvxz"
vset = set(vowels)

next_consonant = {}
for i, ch in enumerate(alphabet):
    if ch in vset:
        continue
    nxt = ch
    for j in range(i + 1, len(alphabet)):
        if alphabet[j] not in vset:
            nxt = alphabet[j]
            break
    next_consonant[ch] = nxt

nearest_vowel = {}
for ch in alphabet:
    if ch in vset:
        continue
    best = vowels[0]
    best_dist = abs(ord(ch) - ord(best))
    for v in vowels[1:]:
        d = abs(ord(ch) - ord(v))
        if d < best_dist or (d == best_dist and v < best):
            best_dist = d
            best = v
    nearest_vowel[ch] = best

res = []
for ch in s:
    if ch in vset:
        res.append(ch)
    else:
        res.append(ch)
        res.append(nearest_vowel[ch])
        res.append(next_consonant[ch])

print("".join(res))