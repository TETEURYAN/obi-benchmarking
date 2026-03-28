import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    N = data[0]
    M = int(data[1])
    strings = data[2:2+M]
    
    digitos_para_letras = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    char_to_digit = {}
    for d, letters in digitos_para_letras.items():
        for ch in letters:
            char_to_digit[ch] = d
    
    count = 0
    n_len = len(N)
    for s in strings:
        if len(s) != n_len:
            continue
        ok = True
        for i, ch in enumerate(s):
            if char_to_digit[ch] != N[i]:
                ok = False
                break
        if ok:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()