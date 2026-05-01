import sys

line = sys.stdin.readline().rstrip('\n')

words = line.split(' ')
decoded_words = []
for word in words:
    decoded = ''
    i = 0
    while i < len(word):
        if word[i] == 'p' and i + 1 < len(word):
            decoded += word[i+1]
            i += 2
        else:
            decoded += word[i]
            i += 1
    decoded_words.append(decoded)

print(' '.join(decoded_words))